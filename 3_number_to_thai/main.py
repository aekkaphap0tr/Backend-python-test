"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""

# ------------------------------------------------------#

from pythainlp.util import num_to_thaiword
try:
    num = int(input("Input : "))
    if num < 0:
        print("number cannot be less than 0")
    elif num <= 10000000:
        print(f"Output : {num_to_thaiword(num)}")
    else:
        print("range number exceeds limit")
except ValueError:
    print("Error positive number")


# ------------------------------------------------------#