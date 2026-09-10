last = 1
current = 1
index = 2
while len(str(current)) < 1000:
    oldlast = last
    last = current
    current = oldlast + last
    index += 1
print(index)