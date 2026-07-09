key = [[3, 3], [2, 5]]

dict1 = {}
dict2 = {}

for i in range(26):
    dict1[chr(i + 65)] = i
    dict2[i] = chr(i + 65)

plain_text = input("Enter the plain text: ").upper()

if len(plain_text) % 2 != 0:
    plain_text += 'X'

signed_plain_text = []

for j in range(len(plain_text)):
    signed_plain_text.append(dict1[plain_text[j]])

block = []
encrypted_text = ""

for i in range(0, len(plain_text), 2):

    block.append([signed_plain_text[i], signed_plain_text[i + 1]])

    current_block = block[-1]

    modified_block = [
        key[0][0] * current_block[0] + key[0][1] * current_block[1],
        key[1][0] * current_block[0] + key[1][1] * current_block[1]
    ]

    modified_block[0] %= 26
    modified_block[1] %= 26

    encrypted_text += dict2[modified_block[0]]
    encrypted_text += dict2[modified_block[1]]

print("Blocks:", block)
print("Encrypted Text:", encrypted_text)