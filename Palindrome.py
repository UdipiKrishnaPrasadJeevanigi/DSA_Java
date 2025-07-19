def Palindrome(num):
    original_num = num
    rev = 0
    while(num > 0):
        rem = num % 10
        rev = (10 * rev) + rem
        num = int(num / 10)
    if rev == original_num:
        return "Given num is a Palindrome"
    else:
        return "Given num is not a Palindrome"
num = int(input("Enter a number : "))
print(Palindrome(num))