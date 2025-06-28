n = 5
for i in range (n):
    row = "" #the row is a string
    for j in range (n):
        row = row + " * " # for every interation the row is concatenate by a *
    print(row)


# second pattern
# *
# * *
# * * *
# * * * *
n = 4
for i in range(n):
    row = ""
    for j in range(i+1):
        row = row + " * "
    print(row)

# third pattern
n=4
for i in range (n):
    row = ""
    for j in range (n):
        row = row + " * "
    n = n-1
    print(row)

# fourth pattern , number pattern
n = 4
for i in range (n):
    row = ""
    for j in range (i+1):
        row = row +" "+ str(j+1)
    print(row)

n = 4
for i in range (n):
    row = ""
    for j in range (n):
        row = row +" "+ str(j+1)
    n = n - 1
    print(row)


# 1
# 2 2
# 3 3 3
# 4 4 4 4
n = 4
for i in range(n):
    row = ""
    for j in range(i+1):
        row = row + str(i+1)
    print(row)


# sixth pattern


n = 4
for i in range(n):
    row = " "
    for j in range(n - (i+1)):
        row = row + " "
    for k in range(i+1):
        row = row + "*"
    print(row)


# 7th pattern

n = 10
toggle = 1
for i in range(n):
    row = ""
    for j in range(i+1):
        row = row  + str(toggle) + " "
        if  toggle == 1:
            toggle = 0
        else:
            toggle = 1
    print(row)