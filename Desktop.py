import pyttsx3
import socket
import json

PORT = 65432

engine = pyttsx3.init()
# Tweak voice/rate/volume here if needed
# engine.setProperty('rate', 150)
# engine.setProperty('volume', 1.0)

def text_to_speech(current_color, complement_color):
    engine.stop()
    engine.say(f'This item is {current_color}. You can pair it with {complement_color}.')
    engine.runAndWait()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("", PORT))
        server.listen()
        print(f"Listening for Pi on port {PORT}...")

        while True:
            try:
                conn, addr = server.accept()
                with conn:
                    print(f"Connected from {addr}")
                    data = b""
                    while chunk := conn.recv(1024):
                        data += chunk
                    payload = json.loads(data.decode("utf-8"))
                    current_color = payload["current_color"]
                    complement_color = payload["complement_color"]
                    print(f"Received: {current_color} / {complement_color}")
                    text_to_speech(current_color, complement_color)
            except Exception as e:
                print(f"Error: {e}, continuing...")
                continue

if __name__ == "__main__":
    start_server()