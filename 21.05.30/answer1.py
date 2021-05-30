# factorial
def f(n):
    if n == 1:
        return 1
    return n * f(n-1)

print(f(n))

#pibo
def pibo(n):
    if n == 0:
        return 0
    elif n==1 or n==2:
        return 1
    return pibo(n-1) + pibo(n-2)

#prime_num
for i in range(n+1):
    result = True
    if i < 2: result = False
    for j in (2,i): 
        if i % j == 0: result = False
    if result: print(i, end='')  