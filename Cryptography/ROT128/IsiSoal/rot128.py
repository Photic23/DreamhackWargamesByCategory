#!/usr/bin/env python3

# 00 01 02 ... FD FE FF
hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]

with open('flag.png', 'rb') as f:
    plain_s = f.read()

# Turns every byte to hex
plain_list = [hex(i)[2:].zfill(2).upper() for i in plain_s]

# Lists every number from 0 to len of plain_list
enc_list = list(range(len(plain_list)))

# Iterates 0 to len of plain_list
for i in range(len(plain_list)):

    # Gets every byte from index 0 to len of plain_list
    hex_b = plain_list[i]

    # Turns hex_b to integer
    index = hex_list.index(hex_b)

    # Puts hex of (index+128) % 256
    enc_list[i] = hex_list[(index + 128) % len(hex_list)]

enc_list = ''.join(enc_list)

with open('encfile', 'w', encoding='utf-8') as f:
    f.write(enc_list)
