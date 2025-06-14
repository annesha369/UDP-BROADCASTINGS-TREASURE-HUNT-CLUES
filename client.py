import socket

def caesar_decrypt(text, shift=3):
    return ''.join(
        chr((ord(c) - 65 - shift) % 26 + 65) if c.isupper() else
        chr((ord(c) - 97 - shift) % 26 + 97) if c.islower() else c
        for c in text
    )

PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))

print("[Client] Listening for broadcasted clues...")
while True:
    data, addr = sock.recvfrom(1024)
    encrypted = data.decode()
    decrypted = caesar_decrypt(encrypted, 3)
    print(f"[Client] Received clue from {addr}: {decrypted}")
