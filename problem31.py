coins = [200, 100, 50, 20, 10, 5, 2, 1]
combinations = [0]*201
combinations[0] = 1
for coin in coins:
    for i in range(len(combinations)):
        if i-coin >= 0:
            combinations[i] += combinations[i-coin]
print(combinations[200])
