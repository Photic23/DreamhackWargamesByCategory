# undefined8 FUN_140001000(longlong param_1)

# {
#   uint local_18;
  
#   local_18 = 0;
#   while( true ) {
#     if (0x1b < local_18) {
#       return 1;
#     }
#     if (((int)(uint)*(byte *)(param_1 + (int)local_18) >> 4 |
#         (*(byte *)(param_1 + (int)local_18) & 0xf) << 4) !=
#         (uint)(byte)(&DAT_140003000)[(int)local_18]) break;
#     local_18 = local_18 + 1;
#   }
#   return 0;
# }

input = "242713c6c61316e647f5269647f54627132626c656f5c3c3f5e3e3"
flag = ""
for i in range(0, len(input), 2):
    flag += chr(int(input[i:i+2][::-1], 16))
print(flag)