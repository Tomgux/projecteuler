import math

numbers = []
for i in range(10, 100000):
    factorialtotal = 0
    for j in range(len(str(i))):
        factorialtotal += math.factorial(int(str(i)[j]))
    if i == factorialtotal:
        numbers.append(i)
print(numbers)
answer = 0
for i in range(len(numbers)):
    answer = answer + numbers[i]
print(answer)