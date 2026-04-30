import pyttsx3
import socket
import json

PORT = 65432

def text_to_speech(current_color, complement_colors):
    # Reinitialize engine each call to avoid conflicts if button is pressed mid-speech
    engine = pyttsx3.init()
    complements = ", ".join(complement_colors)
    engine.say(f'This item is {current_color}. You can pair it with {complements}.')
    engine.runAndWait()
    engine.stop()

def start_server():
    # Start a TCP server that listens for incoming color data from the Pi
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("", PORT))
        server.listen()
        print(f"Listening for Pi on port {PORT}...")

        # Continuously wait for new connections
        while True:
            try:
                conn, addr = server.accept()
                with conn:
                    print(f"Connected from {addr}")

                    # Receive all data from the Pi
                    data = b""
                    while chunk := conn.recv(1024):
                        data += chunk

                    # Parse the JSON payload
                    payload = json.loads(data.decode("utf-8"))
                    current_color = payload["current_color"]
                    complement_colors = payload["complement_colors"]

                    print(f"Received: {current_color} / {complement_colors}")

                    # Speak the result
                    text_to_speech(current_color, complement_colors)

            except Exception as e:
                # If anything goes wrong, log and keep the server running
                print(f"Error: {e}, continuing...")
                continue

if __name__ == "__main__":
    start_server()
    