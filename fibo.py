# def fibo(n:int):

#     if n == 0:
#         return n
    
#     if n == 1:
#         return n
    
#     return fibo(n-1) + fibo(n-2)

# for i in range(50):
#     print(i, fibo(i))

cache = {}
def fibo_opt(n:int):

    if n in cache:
        return cache[n]

    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    value = fibo_opt(n-1) + fibo_opt(n-2)
    cache[n] = value
    return value

# print(fibo_opt(37))

# for i in range(1000):
#     print(i, fibo_opt(i))

print(fibo_opt(970))
