# undefined8 FUN_140001000(longlong param_1)

# {
#   uint local_18;
  
#   local_18 = 0;
#   while( true ) {
#     if (0x11 < local_18) {
#       return 1;
#     }
#     if (*(uint *)(&DAT_140003000 + (longlong)(int)local_18 * 4) !=
#         (uint)*(byte *)(param_1 + (int)local_18)) break;
#     local_18 = local_18 + 1;
#   }
#   return 0;
# }

input = "430000006f0000006d000000700000003400000072000000650000005f0000007400000068000000650000005f0000006100000072000000720000003400000079"
flag = ""
for i in range(0, len(input), 8):
    flag += chr(int(input[i:i+2], 16))
print(flag)