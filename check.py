import hex_to_base64

print('Challenge 1: Hexadecimal to Base64')
print(f'Using String manipulation: {hex_to_base64.hex_to_base64_string('4d61')}')
print(f'Using Bitwise operation: {hex_to_base64.hex_to_base64_bitwise('4d61')}')
print(f'Using Bitwise operation(more concise): {hex_to_base64.hex_to_base64('4d61')}')
