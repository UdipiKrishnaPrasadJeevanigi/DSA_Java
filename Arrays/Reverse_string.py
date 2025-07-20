str = ["K","r","i","s","h","n","a"]
start = 0
end = len(str)/2-1
while start < end:
    # temp = str[start]
    # str[start] = str[end]
    # str[end] = temp
    str[start],str[end] = str[end],str[start]
    start = start + 1
    end = end - 1
print(str)

#Swapping technique
# a_copy = a
# a = b
# b = a_copy