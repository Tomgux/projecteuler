# this answer can be found with a little thought and no code !

print(2*3*2*5*7*2*3*11*13*2*17*19)

# think about it like this: for 2*3*2, the answer is divisible by any number we can make using those 3 numbers, i.e 2, 3, 2*2=4, 2*3=6, 2*2*3=12
# so simply construct the smallest (smallest being the smallest once they are all multiplied together) 
# list of numbers required such that every number 1-20 can be created using some combination in the list.