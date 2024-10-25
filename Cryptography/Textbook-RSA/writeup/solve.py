from pwn import *
from Crypto.Util.number import long_to_bytes

r = remote("host3.dreamhack.games", 20987)

r.recvuntil(b"[3] Get info")
r.sendline(str(3).encode())

r.recvuntil(b"N: ")
N = int(r.recvline())
r.recvuntil(b"e: ")
e = int(r.recvline())
r.recvuntil(b"FLAG: ")
flag_enc = int(r.recvline())

X = (pow(2, e, N) * (flag_enc % N)) % N

r.recvuntil(b"[3] Get info")
r.sendline(str(2).encode())
r.recvuntil(b"Input ciphertext (hex): ")
r.sendline(long_to_bytes(X).hex().encode())

Y = int(r.recvline())

flag = long_to_bytes(Y//2)

print(f"FLAG: {flag.decode()}")