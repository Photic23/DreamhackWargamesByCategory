# source: https://crypto.stackexchange.com/questions/88494/finding-the-iv-of-aes-cbc-ctf

from pwn import *
from Crypto.Util.strxor import strxor
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES

r = remote("host3.dreamhack.games", 17991)

r.recvuntil(b"[3] Get Flag")
r.sendline(str(1).encode())
r.recvuntil(b"Input plaintext (hex): ")

p1 = "aa"*16
p2 = "bb"*16

r.sendline((p1+p2).encode())

raw = r.recvline().decode()

c1 = raw[:32]
c2 = raw[32:]

r.recvuntil(b"[3] Get Flag")
r.sendline(str(2).encode())
r.recvuntil(b"Input ciphertext (hex): ")
r.sendline(c2.encode())
p2_new = r.recvline().decode()

r.recvuntil(b"[3] Get Flag")
r.sendline(str(3).encode())
r.recvuntil(b"flag = ")
flag_enc = r.recvline().decode()

key = strxor(strxor(bytes.fromhex(p2), bytes.fromhex(p2_new)), bytes.fromhex(c1))
flag = unpad(AES.new(key, AES.MODE_CBC, key).decrypt(bytes.fromhex(flag_enc)), 16)
print(f"FLAG: {flag.decode()}")