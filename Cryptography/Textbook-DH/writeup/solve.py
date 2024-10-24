from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

def decrypt_flag(shared_secret: int, ciphertext: str):
    aes_key = hashlib.md5(str(shared_secret).encode()).digest()
    cipher = AES.new(aes_key, AES.MODE_ECB)
    return unpad(cipher.decrypt(bytes.fromhex(ciphertext)), 16)
    
def main():   
    r = remote('host3.dreamhack.games', 9890)

    g = 2
    r.recvuntil(b"Prime: ")
    p = int(r.recvline(), 16)
    r.recvuntil(b"Alice sends her key to Bob. Key: ")
    A = int(r.recvline(), 16)
    
    x1 = 69
    x2 = 420
    y1 = pow(g, x1, p)
    y2 = pow(g, x2, p)

    # Shared secret with Alice
    K2 = pow(A, x2, p)

    r.recvuntil(b">> ")
    r.sendline(f"{y1}".encode('utf-8'))

    r.recvuntil(b"Bob sends his key to Alice. Key: ")
    B = int(r.recvline(), 16)

    # Shared secret with Bob
    K1 = pow(B, x1, p)

    r.recvuntil(b">> ")
    r.sendline(f"{y2}".encode('utf-8'))

    r.recvuntil(b"Alice: ")
    first_half = r.recvline().decode()

    r.recvuntil(b"Bob: ")
    second_half = r.recvline().decode()

    flag = decrypt_flag(K2, first_half) + decrypt_flag(K1, second_half)
    print(f"FLAG: {flag.decode()}")

if __name__ == "__main__":
    main()