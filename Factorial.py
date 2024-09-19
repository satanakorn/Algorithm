#หาผลคูณของจำนวนเต็มตั้งแต่ 1 ถึง n

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n - 1)

n = 4
print(factorial(n))