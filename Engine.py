import ColorDict
import camera
import socket
import json

DESKTOP_PORT = 65432

def get_desktop_ip():
    # Resolve Mac hostname dynamically so we don't need to hardcode an IP
    # This works as long as both devices are on the same network
    import socket as s
    return s.gethostbyname("Makaelas-MacBook-Air-423.local")

def send_colors(current_color, complement_colors):
    # Package the color data as JSON and send to the desktop over a socket
    payload = json.dumps({
        "current_color": current_color,
        "complement_colors": complement_colors
    })
    DESKTOP_IP = get_desktop_ip()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((DESKTOP_IP, DESKTOP_PORT))
        s.sendall(payload.encode("utf-8"))
    print(f"Sent: {current_color} / {complement_colors}")

def main():
    # Take a picture and get the dominant color as RGB
    rgb = camera.takePicture(k=6)

    # Match RGB to closest named color and find complements
    current_color = ColorDict.get_closest_color(rgb)
    complement_colors = ColorDict.get_complement_color(rgb)

    print(f"Detected: {current_color}, Complements: {complement_colors}")

    # Send results to desktop for text to speech
    send_colors(current_color, complement_colors)

if __name__ == "__main__":
    main()
    