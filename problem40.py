digitarray = [0]
for i in range(1, 200000):
    string = str(i)
    for j in range(len(string)):
        digitarray.append(int(string[j]))
print(digitarray[1]*digitarray[10]*digitarray[100]*digitarray[1000]*digitarray[10000]*digitarray[100000]*digitarray[1000000])