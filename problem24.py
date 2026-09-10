digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # permutation 1
# We want to repeatedly find the next permutation and output the millionth#
for i in range(0, 999999):
    location = 9
    while digits[location-1] > digits[location]:
        location = location - 1
    location = location - 1

    rangetoedit = digits[location:]
    oldvalue = digits[location]

    nextvaluelocation = -1
    nextvalue = 10
    for j in range(len(rangetoedit)):
        if rangetoedit[j] > oldvalue:
            if rangetoedit[j] < nextvalue:
                nextvalue = rangetoedit[j]
                nextvaluelocation = j
    rangetoedit[0] = nextvalue
    rangetoedit[nextvaluelocation] = oldvalue

    array = []
    for j in range(1, len(rangetoedit)):
        array.append(rangetoedit[j])
    array.sort()
    digits[location] = rangetoedit[0]
    for j in range(location+1, len(digits)):
        digits[j] = array[j-location-1]

output = ""
for i in range(len(digits)):
    output = output + str(digits[i])

print(output)