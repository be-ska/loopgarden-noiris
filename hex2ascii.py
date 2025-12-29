str = "54 68 65 20 73 6F 6E 67 73 20 77 68 69 73 70 65 72 20 6E 69 6E 65 20 73 65 63 72 65 74 73 2E 20 48 65 61 72 20 74 68 65 6D 20 61 6E 64 20 66 69 6E 64 20 74 68 65 20 77 61 79 20 66 6F 72 77 61 72 64 2E 20 6C 6F 6F 70 67 61 72 64 65 6E 2E 69 6F 2F 78 78 78 78 78 78 78 78 78 2E 7A 69 70"
hex_list = str.split()
ascii_chars = ""
for h in hex_list:
    ascii_chars += chr(int(h, 16))
print(ascii_chars)
