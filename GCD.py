#ตัวหารร่วมมากที่สุดของ 2 ตัวเลข

def GCD(a ,b):
    while b:
        a ,b = b , a % b
    return a

a = 18
b = 27

print("Greatest Common Divisor of", a, "and", b, "is", GCD(a, b)) 

    