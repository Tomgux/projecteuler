import math
# In a 20x20 grid, to reach the bottom right from the top left you will always have to make 20 moves left and 20 moves down.
# So, the question just becomes how many unique combinations of 20 left and 20 down exist (40 choose 20)
answer = math.factorial(40) / (math.factorial(20)*math.factorial(40-20))
print(answer)