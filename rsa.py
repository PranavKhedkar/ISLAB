def gcd(a,b):
    if a == 0:
        return b
    else:
        return gcd(b%a,a)


p = 3
q = 7
n = p*q
phi = (p-1)*(q-1)
e = 2

while(e < phi):
    if (gcd(e,phi) == 1):
        break
    else:
        e = e + 1

k=2
d = (1 + k*phi)//e


msg = 12
print("Message = ",msg)

c = int(pow(msg,e,n))
print("Cipher= ",c)

m = pow(c,d,n)
print("D-msg = ",m)
