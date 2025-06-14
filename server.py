import socket
import time

def caesar_encrypt(text, shift=3):
    return ''.join(
        chr((ord(c) - 65 + shift) % 26 + 65) if c.isupper() else
        chr((ord(c) - 97 + shift) % 26 + 97) if c.islower() else c
        for c in text
    )

clues = [
    "The treasure is buried under the old oak tree.",
    "Look near the riverbank where the rocks form a triangle.",
    "X marks the spot on the north side.",
    "The final clue lies where shadows meet at noon."
]

BROADCAST_IP = '255.255.255.255'
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print("[Server] Broadcasting clues...")
while True:
    for clue in clues:
        encrypted_clue = caesar_encrypt(clue, 3)
        sock.sendto(encrypted_clue.encode(), (BROADCAST_IP, PORT))
        print(f"[Server] Sent clue: {encrypted_clue}")
        time.sleep(5)
