def howmanydivisors(n):
    count = 0
    for i in range(1, n+1):
        if (n/i)%1==0:
            count = count + 1
    return count

def istriangle(n):
    for i in range(1, n):
        if int(n) == int((i*(i+1))/2):
            return True
    return False

array = [0] * 100000000
for i in range(1, 100000000):
    for j in range(i, 100000000, i):
        array[j] += 1

for i in range(len(array)):
    if array[i] > 500:
        if istriangle(i):
            print(i)
            break

# currently stuck... going to move on for now