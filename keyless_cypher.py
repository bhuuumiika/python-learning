plaintext = input("Enter plain text: ")
if len(plaintext)%2 != 0:
    plaintext += 'x'
row1 = list(plaintext[::2])
row2 = list(plaintext[1::2])
matrix = [row1,row2]
print(matrix)
output = ''
for i in range (2):
    for j in range (len(matrix[0])):
        output += matrix[i][j]
print(output)   

def decription(output):
    length = int((len(output)/2))
    row3 = list(output[:length])
    row4 = list(output[length:])
    matrix2 = [row3, row4]
    encrypted = ''
    
    for i in range (len(matrix2[0])):
        for j in range (2):
            encrypted += matrix2[j][i]
    return encrypted

print(decription(output))        
