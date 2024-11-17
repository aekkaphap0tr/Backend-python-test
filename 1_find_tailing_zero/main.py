"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""

# --------------------------------------------------------------------------------------#
try :

    input_number = int(input("Input Number : "))
    count = 0
    Start = 5

    if input_number < 0: {
            print("number can not be negative")
        }
            
    else :
        while input_number >= Start :
            count+= int(input_number/Start)
            Start *= 5

            print(f"Output : {count}")
        
except ValueError:
    print("ต้องการค่าที่เป็นจำนวนเต็ม!!")

# --------------------------------------------------------------------------------------#