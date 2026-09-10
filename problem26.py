def largestcycle(decimal):
    if len(decimal) < 100000:
        return 0
    else:
        for cyclelength in range(1, 1000):
            skip = False
            for j in range(100000-cyclelength-1, 50000, -cyclelength):
                if decimal[j:j+cyclelength] != decimal[j-cyclelength:j]:
                    skip = True
                    break
            if skip == False:
                return cyclelength

from decimal import *

getcontext().prec = 100000

largestcyclesofar = 0
answer = 0
for d in range(1, 1000):
    fulldecimal = Decimal(1)/Decimal(d)
    if len(str(fulldecimal)) > 2:
        decimal = str(fulldecimal)[2:]
        cycle = largestcycle(decimal)
        if cycle > largestcyclesofar:
            answer = d
            largestcyclesofar = cycle

print("d = " + str(answer) + " largest cycle = " + str(largestcyclesofar))