# Method 1: string binary
def hex_to_base64_string(hex):
    bin_hex = bin(int(hex, 16))[2:]
    print('hex string to binary:', bin_hex)
    bin_hex_padded = bin_hex.zfill(4*len(hex)) + '0'*((6-len(hex)%6)%6)
    print('binary padded for base64 conversion:', bin_hex)
    hex_sep = list(map(lambda i: bin_hex_padded[i:i+6], range(0, len(bin_hex_padded), 6)))
    print('binary string broken into 6 bits:', hex_sep)
    hex_sep_int = list(map(lambda b: int(b, 2), hex_sep))
    print('each 6 bits into base 10:', hex_sep_int)
    base64_b10_list = list(map(lambda c: c + (65 if c < 26 else 71 if c < 52 else -4 if c < 62 else -19 if c == 62 else -16), hex_sep_int))
    print('base64 characters in base 10:', base64_b10_list)
    base64_str = ''.join(map(lambda n: chr(n), base64_b10_list))
    print('base64 string w/o padding:', base64_str)
    base64_str_padded = base64_str + '='*((4-len(base64_str)%4)%4)
    print('final base64 string:', base64_str_padded)
    print()
    return base64_str_padded

# Method 2: bitwise operation (prev)
def hex_to_base64_bitwise(hex):
    hex_int = bytes.fromhex(hex)
    ans = ''
    temp = 0
    Base64_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    for i, h in enumerate(hex_int):
        if i%3 == 0:
            ans += Base64_str[h >> 2]
            temp = (h & 3) << 4
        elif i%3 == 1:
            ans += Base64_str[temp | h >> 4]
            temp = (h & 15) << 2
        else:
            ans += Base64_str[temp | h >> 6]
            ans += Base64_str[h & 63]
            temp = 0
    if temp:
        ans += Base64_str[temp]
    ans += '='*((4-len(ans)%4)%4)
    return ans

# Method 3: Bitwise manipulation ()
def hex_to_base64(hex: str | int) -> str:
    hex_int = hex
    if type(hex) is type(str()):
        hex_int = int(hex, 16)
    else:
        hex = str(hex)[2:]
    hex_int <<= (6-(4*len(hex))%6)%6
    Base64_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    ans = ''.join([Base64_str[(hex_int  >> (i*6)) & 63] for i in range(len(hex)*2//3, -1, -1)])
    return ans + '='*((4 - len(ans)%4)%4)