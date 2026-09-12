# For a prime, every combination of a and b is a unique addition
# For a non prime A, it is a unique addition unless A = x^n for x<a, and then it is unique only if x^(n*b) wasn't recorded yet
# Therefore we can setup a dictionary to record all "n's" for some x and then just iterate through all a's and b's

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n/2)+1):
        if n%i==0:
            return False
    return True

dictionary = {}
answer = 0
for a in range(2, 101):
    # Check all roots up to 10th, if root exists, set n = exponent and x = root and continue 
    x = a
    n = 1
    for root in range(2, 11):
        if (a**(1/root))%1 == 0:
            x = a**(1/root)
            n = root
    for b in range(2, 101):
        if dictionary.get(x) == None:
            dictionary[x] = [n*b]
            answer += 1
        else:
            array = dictionary[x]
            if n*b not in array:
                array.append(n*b)
                dictionary[x] = array
                answer += 1
print(answer)