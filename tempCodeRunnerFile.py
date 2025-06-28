def Palindrome(num):
    rev = 0
    while(num > 0):
        rem = num % 10
        rev = (10 * rev) + rem
        print(rev)
        num = num / 10
        print(num)
    if rev == num:
        return "Given num is a Palindrome"
    else:
        return "Given num is not a Palindrome"

print(Palindrome(545))