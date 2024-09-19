#ตรวจสอบว่าข้อความสามารถอ่านจากซ้ายไปขวาได้หรือไม่และขวาไปซ้ายได้เหมือนกันหรือไม่

def is_palindrome(s):
    return  s== s[::-1]

s = "racecar"
print(is_palindrome(s)) 

s = "hello"
print(is_palindrome(s))

