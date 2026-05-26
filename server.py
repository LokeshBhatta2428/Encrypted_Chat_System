import socket
from Crypto.Cipher import AES
import base64

key = b'12345678901234567890123456789012'  # 32-byte key for AES-256

IV = b'1234567890123456'  # 16-byte IV for AES

def decrypt_message(encrypted_message):
    encrypted_message = base64.b64decode(encrypted_message)
    cipher = AES.new(key, AES.MODE_CBC, IV)
    decrypted = cipher.decrypt(encrypted_message)
    return decrypted.decode('utf-8') #No padding removal for simplicity

#create a tcp socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))

printf("Server is listening on port 5000...")
conn, addr = server_socket.accept()
print(f"Connection from {addr} has been established!")

data = conn.recv(1024)
print(f"Encrypted message received: {data.decode()}")

decrypt_text = decrypt_message(data.decode())
print(f"Decrypted message: {decrypt_text}")

conn.close()
server_socket.close()
