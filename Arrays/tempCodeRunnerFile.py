str = ["K","r","i","s","h","n","a"]
start = 0
end = len(str)
for char in range(len(str)):
    str[start] = str[end]
    start = start + 1
    end = end - 1
print(str)