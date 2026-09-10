answer = 0
for i in range(1, 271001):
    square = i*i
    if square%2 == 1:
        answer = answer + square
print(answer)