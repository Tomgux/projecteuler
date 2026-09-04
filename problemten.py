array = [True] * 2000000
array[0] = False
array[1] = False
for i in range(2, 1450):
    for j in range(2*i, 2000000, i):
        array[j] = False

answer = 0
for i, number in enumerate(array):
    if number == True:
        answer = answer + i
print(answer)