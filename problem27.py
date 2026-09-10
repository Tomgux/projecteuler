def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n/2)+1):
        if n%i==0:
            return False
    return True

max = 0
product = 0
for a in range(1, 1000):
    for b in range(1, 1001):
        for sign in range(4): # 0 ++, 1 +-, 2 -+, 3 --
            for n in range(0, 100):
                if sign == 0 or sign == 1:
                    a_2 = a
                else:
                    a_2 = -a
                if sign == 0 or sign == 2:
                    b_2 = b
                else:
                    b_2 = -b
                if isprime((n**2)+(a_2*n)+(b_2)):
                    if n > max:
                        max = n
                        product = a_2 * b_2
                else:
                    break

print(product)