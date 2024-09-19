#สร้างลำดับ Fibonacci ด้วยการหาผลรวมของ 2  ตัวก่อนหน้า

def fibonacci(n):
    if n <= 1:
        return n
    return(fibonacci(n-1) + fibonacci(n-2))


n = 10
print(f"Fibonacci({n}) = {fibonacci(n)}")