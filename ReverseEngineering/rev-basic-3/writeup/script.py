# undefined8 FUN_140001000(longlong param_1)

# {
#   uint local_18;
  
#   local_18 = 0;
#   while( true ) {
#     if (0x17 < local_18) {
#       return 1;
#     }
#     if ((uint)(byte)(&DAT_140003000)[(int)local_18] !=
#         (*(byte *)(param_1 + (int)local_18) ^ local_18) + local_18 * 2) break;
#     local_18 = local_18 + 1;
#   }
#   return 0;
# }
input = "4960677463674266807869697b996d8868949f8d4da59d45"
flag = ""
j = 0
for i in range(0, len(input), 2):
     flag += chr((int(input[i:i+2], 16) - j*2) ^ j)
     j += 1
print(flag)