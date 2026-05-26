import socket
from Crypto.Cipher import AES
import base64
key = b'12345678901234567890123456789012'  # 32-byte key for AES-256
IV = b'1234567890123456'  # 16-byte IV for AES

def encrypt_message(message):
    cipher = AES.new(key, AES.MODE_CBC, IV)
    enrypted = ciph