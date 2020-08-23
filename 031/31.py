# how many ways to compose 200
# this is the coin dp problem
def coin_sums(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    total = 200
    prev, cur = [], []
    for i in range(0, total + 1):
        prev.append(1)
        cur.append(0)

    for i in range(1, len(coins)):
        c = coins[i]
        for j in range(0, len(cur)):
            if j < c:
                cur[j] = prev[j]
            else:
                cur[j] = prev[j] + cur[j - c]
        prev, cur = cur, prev
    return prev[len(prev) - 1]

print(coin_sums(200))
