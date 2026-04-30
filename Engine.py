import ColorDict
import camera
import socket
import json
 
DESKTOP_IP = socket.gethostbyname("Makaelas-MacBook-Air-423.local")  
DESKTOP_PORT = 65432
 
def send_colors(current_color, complement_color):
    payload = json.dumps({
        "current_color": current_color,
        "complement_color": complement_color
    })
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((DESKTOP_IP, DESKTOP_PORT))
        s.sendall(payload.encode("utf-8"))
    print(f"Sent: {current_color} / {complement_color}")
 
def main():
    rgb = camera.takePicture(k=6)
    current_color = ColorDict.get_closest_color(rgb)
    complement_color = ColorDict.get_complement_color(rgb)  
    send_colors(current_color, complement_color)
 
if __name__ == "__main__":
    main()