lastnumber = 1
currentnumber = 2
answer = 0
while currentnumber < 4000000:
    if currentnumber%2 == 0:
        answer = answer + currentnumber
    oldcurrent = currentnumber
    currentnumber = currentnumber + lastnumber
    lastnumber = oldcurrent
print(answer)

# we can simply iterate through all fibonnaci numbers, check the condition, and if met, add it to our sum
    