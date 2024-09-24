with open('encfile', 'r', encoding='utf-8') as f:
    enc_s = f.read()

# Lists every number from 0 to half of len of enc_s
res = list(range(len(enc_s)//2))

# Iterates 0 to len of enc_s with 2 steps
for i in range(0, len(enc_s), 2):

    # Turns hex to integer, minus 128, and mod by 256
    res[i//2] = (int(enc_s[i:i+2], 16)-128)%256

with open('flag.png', 'wb') as f:

    # Turns integers to byte form
    f.write(bytes(res))