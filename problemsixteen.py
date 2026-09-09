# I just calculate 2^X as a string and then add the digits

x = 1000
answer = "1"
for i in range(x):
    carry = 0
    for j in range(len(answer)-1, -1, -1):
        currentdigit = int(answer[j])
        newdigit = currentdigit*2 + carry
        carry = newdigit//10
        newdigit = newdigit - (carry*10)
        answer = answer[0:j] + str(newdigit) + answer[j+1:]
    if carry!=0:
        answer = str(carry) + answer

sumofdigits = 0
for i in range(len(answer)):
    sumofdigits = sumofdigits + int(answer[i])

print(sumofdigits)