def gcd(a, b):
    #calculates the gcd of two integers using the Euclidean algorithm
    b, a = sorted([a, b])
    return gcd(b, a % b) if b else a

def lcm(a, b):
    #calculates lcm of two integers
    b, a = sorted([a, b])
    return a // gcd(a, b) * b

def addFractions(num1, den1, num2, den2):
    #adds two fractions and reduces the result
    num3 = num1*den2 + num2*den1
    den3 = den1*den2
    return num3 // gcd(num3, den3), den3 // gcd(num3, den3)
