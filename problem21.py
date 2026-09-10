def d(n):
    count = 0
    for i in range(1, n):
        if n%i==0:
            count += i
    return count

numbersfound = {}
answer = 0
for i in range(1, 10000):
    b = d(i)
    if d(b) == i and (b!=i):
        if numbersfound.get(i) == None:
            answer = answer + i
            numbersfound[i] = True
        if numbersfound.get(b) == None:
            answer = answer + b
            numbersfound[b] = True

print(answer)