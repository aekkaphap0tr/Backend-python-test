"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""

#--------------------------------------------------------------------------#

try :

    list = [10,20,30,40,-50]
    
    max_value = max(list)

    index = list.index(max_value)

    print(f"Output : {index}")
        
except ValueError:
    print("list can not blank")

#--------------------------------------------------------------------------#