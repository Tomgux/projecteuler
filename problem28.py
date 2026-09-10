sum = 25 # initial sum
currentnumber = 9
for sidelength in range(5, 1003, 2):
    for i in range(4):
        currentnumber = currentnumber + sidelength - 1
        sum = sum + currentnumber

print(sum)