def ispalindrome(n):
    string = str(n)
    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

def decimaltobinary(n):
    highestpower = 0
    while 2**highestpower <= n:
        highestpower += 1
    highestpower -= 1
    number = n
    answer = ""
    while highestpower>=0:
        if number>=(2**highestpower):
            answer = answer + "1"
            number = number - (2**highestpower)
        else:
            answer = answer + "0"
        highestpower -= 1
    return answer

answer = 0
for i in range(1,1000000):
    if ispalindrome(i):
        if ispalindrome(decimaltobinary(i)):
            answer += i
print(answer)