import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad  
import base64

key = b'12345678901234567890123456789012'  # 32-byte key for AES-256
IV = b'1234567890123456'  # 16-byte IV for AES

def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_CBC, IV)
    
    # Convert string to raw bytes
    message_bytes = message.encode('utf-8')
    
    # FIX: Automatically pads the data to a multiple of 16 bytes
    padded_bytes = pad(message_bytes, AES.block_size)
    
    encrypted = cipher.encrypt(padded_bytes)
    return base64.b64encode(encrypted).decode('utf-8')

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

# Prompt can now take any message length safely
message = input("Enter your message: ")

encrypted_text = encrypt_message(message)
print(f"Encrypted message to send: {encrypted_text}")

client_socket.sendall(encrypted_text.encode('utf-8'))

client_socket.close()


