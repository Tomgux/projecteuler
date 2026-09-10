# Calculate x! as a string and then iterate through and sum the digits. 

x = 100
answer = "1"
for i in range(2, x+1):
    carry = 0
    for j in range(len(answer)-1, -1, -1):
        currentdigit = int(answer[j])
        newdigit = currentdigit*i + carry
        carry = newdigit//10
        newdigit = newdigit - (carry*10)
        answer = answer[0:j] + str(newdigit) + answer[j+1:]
    if carry!=0:
        answer = str(carry) + answer

sumofdigits = 0
for i in range(len(answer)):
    sumofdigits = sumofdigits + int(answer[i])

print(sumofdigits)