import math
def destination(p, q, cyphertext):
    n = p*q
    fn = (p-1)*(q-1)
    for i in range (2, fn):
        if math.gcd(i,fn)==1:
            e = i
            break
    for j in range (fn):
        if (e * j) % fn == 1:
            d = j
            break
    if cyphertext == None:
        return e , n
    
    else:
        M = pow(cyphertext,d,n)
        return M



def source(e , n, plaintext):
    C = pow(plaintext, e, n)
    return C


P = int(input("Enter a prime no. p: "))
Q = int(input("Enter a prime no. q: "))
e , n= destination(P,Q, None)
print("Enter message you want to encrypt which is less than :",n)
plaintext = int(input())
Cyphertext = source(e ,n, plaintext )
print( "Your cyphertext is: ", Cyphertext)
decrypted_text = destination(P, Q, Cyphertext)
print("After decryption the plaintext is: ", decrypted_text)
