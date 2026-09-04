array = [True] * 200000
for i in range(2, 450):
    for j in range(2*i, 200000, i):
        array[j] = False

primecount = 0
for i, number in enumerate(array):
    if number == True:
        primecount = primecount + 1
        if primecount == 10003: # added two because this setup "includes" 0 and 1 as primes
            print(i)
            break