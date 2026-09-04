# loop through valid palindromes and check if they have a valid pair of 3 digit factors
# continue until the palindromes become so large that this pair couldn't possibly exist (i.e palindrome > 998001)

def intopalindrome(n):
    firsthalf = str(n)
    output = str(n)
    for i in range(len(firsthalf)-1, -1, -1):
        output = output + firsthalf[i]
    return int(output)

firsthalf = 1
palindrome = intopalindrome(firsthalf)
answer = 1
while palindrome < 998001:
    palindrome = intopalindrome(firsthalf)
    for i in range(100, 1000):
        if (palindrome/i)%1==0:
            if palindrome/i < 1000:
                answer = palindrome
                break
    firsthalf = firsthalf + 1
print(answer)
