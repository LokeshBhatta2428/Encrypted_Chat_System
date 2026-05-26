import socket
from Crypto.Cipher import AES
import base64

key = b'12345678901234567890123456789012'  # 32-byte key for AES-256
IV = b'1234567890123456'  # 16-byte IV for AES

def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_CBC, IV)
    enrypted = cipher.encrypt(message.encode('utf-8'))
    return base64.b64encode(enrypted).decode('utf-8')

# Create a TCP socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))
message = input ("Enter a 16 bytes message:  ")
encrypted_text = encrypt_message(message)
print(f"Encrypted message to send: {encrypted_text}")
client_socket.sendall(encrypted_text.encode())

client_socket.close()

