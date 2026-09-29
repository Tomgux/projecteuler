def ispandigital(m):
    string = str(m)
    if len(string) != 9:
        return False
    else:
        array = [False] * 9
        for i in range(9):
            array[(int(string[i])-1)] = True
        for i in range(len(array)):
            if array[i] == False:
                return False
        return True

def returnpandigitalproduct(m):
    n = 2
    string = str(m)
    answer = string
    while len(answer) < 10:
        if len(answer + str((m*n))) < 10:
            answer = answer + str((m*n))
            n += 1
        else:
            break
    if ispandigital(answer):
        return int(answer)
    else:
        return 0

answer = 0
index = 0
for i in range(1000000):
    number = returnpandigitalproduct(i)
    if number>answer:
        index = i
        answer = number
print(answer)
print(index)
