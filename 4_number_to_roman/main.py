"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""

#--------------------------------------------------------------#

import roman
try:
    num = int(input("Input : "))
    if num < 0:
        print("number cannot be less than 0")
    else :
        print(f"Output : {roman.toRoman(num)}")
except ValueError:
    print("number can not less than 0")


#--------------------------------------------------------------#
