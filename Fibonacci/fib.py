import time

def fib(n, memo={}):
    if (n in memo):
        return memo[n]
    if n<=2:
        return 1

    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(7))
print(fib(15))
start_time = time.time()
print(fib(100))
print("--- %s seconds ---" % (time.time() - start_time))

