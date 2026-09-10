rawdata = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle = [[int(num) for num in line.split()] for line in rawdata.strip().splitlines()]

maxarray = [[75]]

for i in range(1, len(triangle)):
    newaddition = []
    for j in range(len(triangle[i])):
        if j == 0:
            newaddition.append(maxarray[i-1][0]+triangle[i][j])
        elif j == len(maxarray[i-1]):
            newaddition.append(maxarray[i-1][-1]+triangle[i][j])
        else:
            newaddition.append(max(maxarray[i-1][j-1]+triangle[i][j], maxarray[i-1][j]+triangle[i][j]))

    maxarray.append(newaddition)

max = 0
for i in range(len(maxarray[-1])):
    if maxarray[-1][i] > max:
        max = maxarray[-1][i]

print(max)

# We figure out the maximum value you can have when ending at a specific position in the triangle. 
# We calculate these top down and store them in maxarray.
# The final answer is simply the largest number in the final row of maxarray

        


