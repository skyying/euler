import time

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# Which starting number, under one million, produces the longest chain?

" remember what has been calculate "

produced = {}
def produce_chain(n):
    if n in produced:
        return produced[n]
    step = 1
    start = n
    while start != 1:
        if start in produced:
            step += produced[start]
            produced[n] = step
            return step
        elif start % 2 == 0: 
            start = start / 2
            step += 1
        else:
            start = (start * 3) + 1
            step += 1
    produced[n] = step
    return step

start = 1500

# 1, 
# 13, 10
# 14, 18
# 15, 18


def start_calc():
    mm = 0
    step = 0
    n = 0
    for i in range(500000, 1000000):
      step = produce_chain(i)
      if step > mm:
        mm = step
        n = i
    return n

start = time.time()
print(start_calc())
print(time.time() - start)





