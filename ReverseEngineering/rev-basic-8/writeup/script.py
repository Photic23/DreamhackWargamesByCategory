
# undefined8 FUN_140001000(longlong param_1)

# {
#   uint local_18;
  
#   local_18 = 0;
#   while( true ) {
#     if (0x14 < local_18) {
#       return 1;
#     }
#     if ((char)(*(char *)(param_1 + (int)local_18) * -5) != (&DAT_140003000)[(int)local_18]) break;
#     local_18 = local_18 + 1;
#   }
#   return 0;
# }

input = "acf30c25a310b72516c6b7bc072502d5c61107c5"

flag = ""
for i in range(0, len(input), 2):
    hex = int(input[i:i+2], 16)

    # We need to brute force all ascii value because
    # (char)(*(char *)(param_1 + (int)local_18) * -5)
    # can result in an overflow. So, reversing the operation
    # might not give the original value.
    for j in range(2**8):

        # I use &0b11111111 to get only 1 byte
        if (j * -5)&0b11111111 == hex:
            flag += chr(j)
            break
print(flag)

