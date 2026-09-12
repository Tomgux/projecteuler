answer = 0
for i in range(2, 100000000):
    sum = 0
    for j in range(len(str(i))):
        sum = sum + int(str(i)[j])**5
    if i == sum:
        answer = answer + i
print(answer)