def isvalid(a,b,c):
    if c**2==(a**2)+(b**2):
        return True
    else:
        return False
    
def numberofsolutions(p):
    number = 0
    for a in range(1, p):
        for b in range(a, p):
            if a>0 and b>0 and (p-a-b)>0:
                if isvalid(a,b,p-a-b):
                    number += 1
    return number

answer = 0
amount = 0
for p in range(1, 1001):
    newamount = numberofsolutions(p)
    if newamount>amount:
        amount = newamount
        answer = p
print(answer)