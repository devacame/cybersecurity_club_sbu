import hex_to_base64
import data_entropy

print("Challenge 1: Hexadecimal to Base64")
print(f'Using String manipulation: {hex_to_base64.hex_to_base64_string('4d61')}')
print(f'Using Bitwise operation: {hex_to_base64.hex_to_base64_bitwise('4d61')}')
print(f'Using Bitwise operation(more concise): {hex_to_base64.hex_to_base64('4d61')}')

print("Challenge 2: Calculate Randomness of data")
check_data = [
    "6f6664797a7179636f75797362636c6c6b686d68797a6d",
    "67686c666a776874726979726e726a7361796d766b787a",
    "65736167686d777975796a7563676a7a6a63616b6a656e",
    "61647a6e7566687373677571717763736b746a716d6c67",
    "76796378616f786875776c62706d6d676c6a6767696a6e",
    "6d78717275756b726466657975626675766f6a6370697a",
    "666b6764636b706c6662717676776979676879726f7276",
    "7371716868747576706a6c636f68796b78667473797279",
    "79616a65777070756572737575717470726f696d686d66",
    "70696e656170706c6520756e6465722074686520736561",
    "61617678707576776a6e6962746b757768776464617870",
    "63756c666f7364706267717462706c7a7463686d6e7672",
    "646d7376787569626364736c7a69636467796264766368",
    "756b7872716c69666a656271787a6e626464796c667066",
    "7976716769666a6a73776977796a7a68746c6f7a6c6a7a",
    "6b74666a6e6376646862757a6c6c76657870717773776e",
    "72617a6967706b62746179716e6e676368677567686d74",
    "7074766b646d6f6a7579756a776a677a75786275667871",
    "6970757868717866756e677763697067696e746e6b7870",
    "726a696273707a69726a67756c71666c77737779746d72",
]
entropy_vals = [data_entropy.calculateEntropy(data) for data in check_data]
for data, entropy in zip(check_data, entropy_vals):
    print(f'Entropy of {data} is {entropy} (text is {data_entropy.hex_to_text(data)})')
print(f'Entropy of printable ascii characters is {data_entropy.ASCII_ENTROPY}')
lowest_entropy_data = check_data[entropy_vals.index(min(entropy_vals))]
print(f'Data with the lowest entropy is {lowest_entropy_data} with text: {data_entropy.hex_to_text(lowest_entropy_data)}')