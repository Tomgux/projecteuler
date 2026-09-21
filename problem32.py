dictionary = {}
answer = 0
for a in range(1, 9999):
    for b in range(1, 999):
        c=a*b
        numbers = str(a)+str(b)+str(c)
        if len(numbers) != 9:
                    continue
        array = [False]*(len(numbers)+1)
        valid = True
        for i in range(len(numbers)):
            if int(numbers[i]) == 0:
                valid = False
            if array[int(numbers[i])] == True:
                  valid = False
            else:
                array[int(numbers[i])] = True
        if valid:
            if dictionary.get(c) == None:
                print(str(a)+" "+str(b)+" "+str(c))
                answer = answer + c
                dictionary[c] = 1
print(answer)
            