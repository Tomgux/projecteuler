targetnumber = 600851475143

# reduce the number by prime factors as we find them !

def isprime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True

currentnumber = 600851475143
checkfactor = 2
answer = 1
while currentnumber > 1:
    if isprime(checkfactor):
        if currentnumber%checkfactor == 0:
            currentnumber = currentnumber/checkfactor
            answer = checkfactor
    checkfactor = checkfactor + 1
print(answer)

# since we check primes starting from 1 and moving up, our answer is always the latest factor we have found.