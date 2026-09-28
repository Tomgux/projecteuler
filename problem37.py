primes = [True] * 1000000

primes[0] = False
primes[1] = False
for i in range(2, 1001):
    for j in range(i+i, 1000000, i):
        primes[j] = False

def isprime(n, primes):
    if primes[n]:
        return True
    else:
        return False

def truncatableprime(n, primes):
    if isprime(n, primes) == False:
        return False
    string = str(n)
    for i in range(len(string)):
        if isprime(int(string[i:]), primes) == False:
            return False
    for i in range(len(string)):
        if isprime(int(string[:i+1]), primes) == False:
            return False
    return True

count = 0
sum = 0
for i in range(10, 1000000):
    if truncatableprime(i, primes):
        count += 1
        sum += i
print(count)
print(sum)