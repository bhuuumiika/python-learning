plaintext = input("Enter the plain text: ").upper()

hexadecimal_values = [format(ord(char), '02X') for char in plaintext]
if len(hexadecimal_values) < 16:
    hexadecimal_values += ['0B'] * (16 - len(hexadecimal_values))
Round_key = ['89', '55', 'B5', 'CE', 'BD', '20', 'E3', '46', '8C', 'C2', 'F1', '46', '9F', '68', 'A5', 'C1']
binary_roundkey = [(int(value, 16)) for value in Round_key]
binary_hexadecimal_values = [int(value, 16) for value in hexadecimal_values]
#Pre-round processing
def pre_round_processing(binary_hexadecimal_values, binary_roundkey):
    pre_round = []
    for i in range(16):
        pre_round.append(binary_hexadecimal_values[i] ^ binary_roundkey[i])
    pre_round = [format(value, '02X') for value in pre_round]
    return pre_round

print("Pre-round processing result: ", pre_round_processing(binary_hexadecimal_values, binary_roundkey))
