primes = [True] * 1000000

primes[0] = False
for i in range(2, 1000):
    for j in range(i+i, 1000000, i):
        primes[j] = False

def isprime(n, primes):
    if primes[n]:
        return True
    else:
        return False

def circularprime(n, primes): # 123
    if n == 1:
        return False
    n = str(n)
    for i in range(len(n)):
        if isprime(int(n), primes) != True:
            return False
        n = n[1:]+n[0]
    return True

count = 0
for n in range(2,1000000):
    if circularprime(n, primes):
        count += 1
print(count)
