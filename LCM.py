#หาตัวคูณร่วมน้อยที่สุดของ 2 ตัวเลข

def GCD(a ,b):
    while b:
        a ,b = b , a % b
    return a




def lcm(a,b):
    return a * b // GCD(a,b)

num1 = 12
num2 = 24
print(lcm(num1,num2))  # Output: 24