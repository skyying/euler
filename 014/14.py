
# this takes about 4.x seconds to run

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

def start_calc():
    mm = 0
    step = 0
    n = 0

    # produce_chain(n) = 1 + produce_chain(n/2) when n is even
    for i in range(500000, 1000000):
      step = produce_chain(i)
      if step > mm:
        mm = step
        n = i
    return n

print(start_calc())





