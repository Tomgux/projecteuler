answer = 0
for i in range(1, 1000):
    if i%3==0 or i%5==0:
        answer = answer + i
print(answer)

# we can simply loop through every possibility, check the condition, and add it to our sum