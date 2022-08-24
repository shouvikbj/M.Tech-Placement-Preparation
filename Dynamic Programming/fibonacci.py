import time

memo = {}


def fib(n):
    if n <= 2:
        return 1
    else:
        if n in memo.keys():
            return memo[n]
        else:
            memo.update({n: fib(n - 1) + fib(n - 2)})
            return memo[n]


t1 = time.time()
print(fib(50))
t2 = time.time()
print(t2 - t1)
# print(memo)
