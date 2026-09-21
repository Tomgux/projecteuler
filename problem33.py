# Try to use an array for numerator and array for denominator when checking the "false" fraction
answer = []
for a in range(10,101):
    for b in range(a,101):
        value = a/b
        numarray = []
        denomarray = []
        for i in range(2):
            numarray.append(str(str(a)[i]))
        for i in range(2):
            denomarray.append(str(str(b)[i]))
        for i in range(len(numarray)):
            for j in range(len(denomarray)):
                if numarray[i] == denomarray[j]:
                    numarray[i] = "N"
                    denomarray[j] = "N"
        numerator = ""
        denominator = ""
        for i in range(2):
            if numarray[i] != "N":
                numerator = numerator + str(numarray[i])
        for i in range(2):
            if denomarray[i] != "N":
                denominator = denominator + str(denomarray[i])
        if numerator != "" and denominator != "":
            numerator = int(numerator)
            denominator = int(denominator)
            if denominator != 0:
                if numerator/denominator == value:
                    if len(str(numerator)) == 1 and len(str(denominator)) == 1:
                        if str(a)[1] != "0" and str(b)[1] != "0":
                            answer.append([a,b])
        totalnumerator = 1
        totaldenominator = 1
        for i in range(len(answer)):
            totalnumerator = totalnumerator * answer[i][0]
            totaldenominator = totaldenominator * answer[i][1]
        for i in range(1000,1,-1):
            if totalnumerator%i == 0 and totaldenominator%i == 0:
                totalnumerator = totalnumerator/i
                totaldenominator = totaldenominator/i
print(answer)
print(totalnumerator)
print(totaldenominator)