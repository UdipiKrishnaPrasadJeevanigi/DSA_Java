



import math
def countDigits(num):
    count = 0
    if num == 0:
        return 1
    while(num > 0):
        num = math.floor(num/10)
        count = count + 1
    return "The Count of number of digits : " + str(count)

num_tst = math.fabs(int(input()))
print(countDigits(num_tst))

# what if the number is zero
# what if the number is less than zero

# math.abs() , math.round() , math.ceil(), math.floor()