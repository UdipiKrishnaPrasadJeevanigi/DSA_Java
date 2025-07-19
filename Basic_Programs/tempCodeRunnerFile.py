def palindrome_for_negative(num):
    num_copy = num
    rev = 0
    num_abs = abs(num)
    while(num_abs > 0):
        rem = num_abs % 10
        rev = (rev * 10) + rem
        num_abs = int(num_abs / 10)

    limit = 2^31
    if(limit < 2^31 or limit > 2^31):
        return 0
    
    rev = -rev if num_copy < 0 else rev
    return rev

Num = int(input("Enter a number :"))
status = palindrome_for_negative(Num)
if(status == Num):
    print("Given Number is a Palindrome")
else:
    print("Given Number is not a Palindrome")
