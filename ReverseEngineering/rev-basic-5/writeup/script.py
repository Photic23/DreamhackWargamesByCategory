
# undefined8 FUN_140001000(longlong param_1)

# {
#   uint local_18;
  
#   local_18 = 0;
#   while( true ) {
#     if (0x17 < local_18) {
#       return 1;
#     }
#     if ((uint)*(byte *)(param_1 + (int)local_18) + (uint)*(byte *)(param_1 + (int)(local_18 + 1)) !=
#         (uint)(byte)(&DAT_140003000)[(int)local_18]) break;
#     local_18 = local_18 + 1;
#   }
#   return 0;
# }

## this is the bruteforce way. just find the readable flag hehe.
# input = "add8cbcb9d97cbc492a1d2d7d2d6a8a5dcc7ada3a1984c"

# for i in range(2**8):
#     flag = chr(i)
#     temp = i
#     for j in range(0, len(input), 2):
#         temp = int(input[j:j+2], 16) - temp
#         try:
#             flag += chr(temp)
#         except:
#             break
#     if len(flag) == len(input)//2+1:
#         print(flag)

# I added extra 00 because there should be 0x18 bytes or 24 bytes
# So, flag[-1] + flag[-2] == 0x00 -> flag[-2] == 0x00
# and flag[-2] + flag[-3] == 0x4c -> flag[-3] == 0x4c
# and so on 
input = "add8cbcb9d97cbc492a1d2d7d2d6a8a5dcc7ada3a1984c00"

flag = ""
temp = 0x00 # this value is flag[-1]
for i in range(0, len(input), 2):
    # capturing the flag from the back
    temp = int(input[len(input)-i-2:len(input)-i], 16) - temp
    flag += chr(temp)

# reverse the flag
print(flag[::-1])