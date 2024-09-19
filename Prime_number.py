#ครวจสอบว่าตัวเลขเป็นจำนวนเฉพาะหรือไม่

def prime_number(n):
    if n <= 1:
        return False
    for i in  range(2 , int(n**0.5) +1):
        if n %  i == 0:
            return False
        
    return True


print(prime_number(15))
print(prime_number(23))
print(prime_number(2))  
print(prime_number(1)) 
