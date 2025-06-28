import math

# def find_largest_number(number_list):
#     max_num = number_list[0]
#     for num in number_list:ṇ
#         if num > max_num:
#             max_num = num
#     return max_num

# simple function to get second largest number from the list.

def second_largest(number_list):
    num_list_length = len(number_list)
    if num_list_length < 2:
        return "Array should have atleast two numbers"

    first_largest = -math.inf
    second_largest = -math.inf
    for num in number_list:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num
    
    return second_largest

# second_largest_num = second_largest([14,9,10,2,8,7,1])
# second_largest_num = second_largest([14])
second_largest_num = second_largest([-14,-9,-10,-2,-8,-7,-14])
print("The second largest number in the list : " + str(second_largest_num))