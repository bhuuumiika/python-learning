key = [["M", "O", "N", "A", "R"],
       ["C", "H", "Y", "B", "D"],
       ["E", "F", "G", "I/J", "K"],
       ["L", "P", "Q", "S", "T"],
         ["U", "V", "W", "X", "Z"]]

def encryption(text):
    text = text.upper()
    new_text = ""
    i = 0
    while i < len(text):
        if i +1 < len(text):
            if text[i] == text[i + 1]:
                new_text += text[i] + 'X'
                i += 1
                continue
            else:
                new_text += text[i] + text[i+1]
        else:
            new_text += text[i]

        i += 2        
    if len(new_text) % 2 != 0:
        new_text += 'X'
    #Encryption process
    encrypted_text = ""
    
    for k in range(0, len(new_text), 2):
        for i in range(5):
            for j in range(5):
                if new_text[k] in key[i][j]:
                    row1, col1 = i, j
                if new_text[k + 1] in key[i][j]:    
                    row2, col2 = i, j
        if row1 == row2:
            encrypted_text += key[row1][(col1+1)%5] + key[row2][(col2+1)%5]

        elif col1 == col2:
            encrypted_text += key[(row1+1)%5][col1] + key[(row2+1)%5][col2] 
        else:
            encrypted_text += key[row1][col2] + key[row2][col1]
    return encrypted_text           
        

        
text = input("Enter text to encrypt: ")
encrypted_text = encryption(text)
print("Encrypted text:", encrypted_text)         

def decryption(encrypted_text):
    row1 = col1 = row2 = col2 = -1
    decrypted_text = ""
    for k in range(0, len(encrypted_text), 2):
        for i in range(5):
            for j in range(5):
                if encrypted_text[k] in key[i][j]:
                    row1, col1 = i, j
                if encrypted_text[k + 1] in key[i][j]:    
                    row2, col2 = i, j
        if row1 == row2:
            decrypted_text += key[row1][(col1-1)%5] + key[row2][(col2-1)%5]
        elif col1 == col2:
            decrypted_text += key[(row1-1)][col1] + key[(row2-1)][col2]
        else:
            decrypted_text += key[row1][col2] + key[row2][col1]
    return decrypted_text   

decrypted_text = decryption(encrypted_text)
print("Decrypted text:", decrypted_text)    
