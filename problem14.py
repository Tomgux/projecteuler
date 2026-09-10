def collatzlength(n):
    count = 1
    while n != 1:
        if n%2==0:
            n = n/2
            count += 1
        else:
            n = (3*n) + 1
            count += 1
    return count

best = -1
number = -1
for i in range(1, 1000000):
    chainlength = collatzlength(i)
    if chainlength > best:
        number = i
        best = chainlength
print(number)

               
        