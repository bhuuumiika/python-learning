dict = {}
for i in range (26):
    dict[i] = chr(i + 65)
print(dict)  
text = input("Enter text to encrypt: ")
new_text=""
if len(text) % 2 != 0:
    for i in range(len(text)):
        if not i == len(text) - 1:
            if text[i] == text[i+1]:
                new_text += text[i] + 'X'
                continue
else: new_text = text            
if len(new_text) % 2 != 0 and new_text[-1] != 'X':
    new_text += new_text[-1] + 'X'
