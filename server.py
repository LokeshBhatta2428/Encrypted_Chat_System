import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

key = b'12345678901234567890123456789012'  # 32-byte key for AES-256
IV = b'1234567890123456'  # 16-byte IV for AES

def decrypt_message(encrypted_message_str):
    # Decode the base64 string back to encrypted bytes
    encrypted_bytes = base64.b64decode(encrypted_message_str)
    
    # Initialize the cipher
    cipher = AES.new(key, AES.MODE_CBC, IV)
    
    # Decrypt and strip the PKCS7 padding
    decrypted_padded = cipher.decrypt(encrypted_bytes)
    decrypted_clean = unpad(decrypted_padded, AES.block_size)
    
    return decrypted_clean.decode('utf-8')

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))


server_socket.listen(1) 

print("Server is listening on port 5000...")
conn, addr = server_socket.accept()
print(f"Connection from {addr} has been established!")

# Receive raw bytes from the network
data = conn.recv(1024)
incoming_text = data.decode('utf-8')
print(f"Encrypted message received (Base64): {incoming_text}")


try:
    decrypt_text = decrypt_message(incoming_text)
    print(f"Decrypted message: {decrypt_text}")
except Exception as e:
    print(f"Decryption failed: {e}")

conn.close()
server_socket.close()


