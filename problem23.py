# We want to know the sum of every number between 1 and 28123 that cannot be written as the sum of two abundant numbers.
# To accomplish this, we can find every abundant number from 1 to 28123, and then relatively quickly check whether a number is capable
# of being a sum of two of these, or not

def isabundant(n):
    count = 0
    for i in range(1, n):
        if n%i==0:
            count += i
    if count > n:
        return True
    else:
        return False
    
abundantnumbers = []
for i in range(1, 28124):
    if isabundant(i):
        abundantnumbers.append(i)

sum = 0
for i in range(1, 28124):
    target = i
    left = 0
    right = len(abundantnumbers)-1
    creatable = False
    while left <= right:
        if abundantnumbers[right]+abundantnumbers[left] == target:
            creatable = True
            break
        if abundantnumbers[right]+abundantnumbers[left] < target:
            left = left + 1
        else:
            right = right - 1
    if creatable == False:
        sum = sum + target

print(sum)

