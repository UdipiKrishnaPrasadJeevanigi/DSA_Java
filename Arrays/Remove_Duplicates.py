
#Here the number of unique elements in the array is 5 i.e(0,1,2,3,4)
def remove_duplicates(arr_):
    x = 0
    for i in range(len(arr_)):
        if(arr_[i] > arr_[x]):
            x = x + 1
            arr_[x] = arr_[i]
    return x+1

arr = [0,0,1,1,1,2,2,2,3,3,4]
unique_elements = remove_duplicates(arr)
print("The number of unique elements : ",unique_elements)