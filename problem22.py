f = open("0022_names.txt")
string = f.read().lower()
array = string.split(",")
array.sort()

answer = 0
for i in range(len(array)):
    sum = 0
    for j in range(len(array[i])):
        if (ord(array[i][j]) - 96) > 0:
            # print("Current sum: "+str(sum)+" Letter: "+str(array[i][j])+" Proposed value: "+str((ord(array[i][j]) - 96)))
            sum = sum + (ord(array[i][j]) - 96)
    answer = answer + (sum*(i+1))
    # print(answer)

print(answer)
f.close()