n=11 #Let
g=3  #Let
x = int(input())
y = int(input())
def source(x,B):
    A = (g**x) % n
    if B is None:
        return A
    
    k1 = (B**x) % n
    return A, k1

def destination(y, A):
    
    B = (g**y) % n
    if A is None:
        return B
    k2 = (A**y) % n
    return B, k2

A = source(x, None)
B = destination(y, None)
_,k1 = source(x, B)
_,k2 = destination(y, A)
print(f"A is: {A}\nB is: {B}\nk1 is: {k1}\nk2 is: {k2}")
