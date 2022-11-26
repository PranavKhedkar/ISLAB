def gcd(a,b):
    if a == 0:
        return b
    else:
        return gcd(b%a,a)

a = int(input("Enter numb 1:"))
b = int(input("Enter numb 2:"))

print("GCD = ",gcd(a,b))
