
# undefined8 FUN_140001000(longlong param_1)

# {
#   uint local_18;
  
#   local_18 = 0;
#   while( true ) {
#     if (0x11 < local_18) {
#       return 1;
#     }
#     if ((&DAT_140003020)[*(byte *)(param_1 + (int)local_18)] != (&DAT_140003000)[(int)local_18])
#     break;
#     local_18 = local_18 + 1;
#   }
#   return 0;
# }

input1 = "004d5150effbc3cf92454dcff50440504363"
input2 = "637c777bf26b6fc53001672bfed7ab76ca82c97dfa5947f0add4a2af9ca472c0b7fd9326363ff7cc34a5e5f171d8311504c723c31896059a071280e2eb27b27509832c1a1b6e5aa0523bd6b329e32f8453d100ed20fcb15b6acbbe394a4c58cfd0efaafb434d338545f9027f503c9fa851a3408f929d38f5bcb6da2110fff3d2cd0c13ec5f974417c4a77e3d645d197360814fdc222a908846eeb814de5e0bdbe0323a0a4906245cc2d3ac629195e479e7c8376d8dd54ea96c56f4ea657aae08ba78252e1ca6b4c6e8dd741f4bbd8b8a703eb5664803f60e613557b986c11d9ee1f8981169d98e949b1e87e9ce5528df8ca1890dbfe6426841992d0fb054bb16"
input2arr = [input2[i:i+2] for i in range(0, len(input2), 2)]
flag = ""

for i in range(0, len(input1), 2):
    flag += chr(input2arr.index(input1[i:i+2]))
print(flag)