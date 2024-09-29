from cipher import STREAM

encryptedDH = "3cef"
plaintextDH = "DH"
last8BitsReversed = bin(int("3c", 16) ^ ord('D'))[2:].zfill(8)
first8BitsReversed = bin(int("ef", 16) ^ ord('H'))[2:].zfill(8)

seed = ""
for i in range(1, 9):
    seed += first8BitsReversed[-i]
for i in range(1, 9):
    seed += last8BitsReversed[-i]
print(f"Seed: 0b{seed} or {int('0b' + seed, 2)}")

output = "3cef03c64ac240c349971d9e4c951cc14ec4199f409249c21e964ac540c540944f901c934cc240934d96419f4b9e4d9f1cc41dc61dc34e9219c31bc11a914f9141c61ada"
outputBytes = bytes([int(output[i:i+2], 16) for i in range(0, len(output), 2)])
stream = STREAM(int('0b' + seed, 2), 16)
print(stream.decrypt(outputBytes).decode("utf-8"))

