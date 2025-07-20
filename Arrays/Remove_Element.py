# Approach used : Two pointer approach
#Problem link : https://leetcode.com/problems/remove-element/description/

def remove_element(arr,val_num):
    x = 0
    for i in range(len(arr)):
        if(arr[i] != val_num):
            arr[x] = arr[i]
            x = x + 1
    return x
nums = [0,0,1,1,3,4,5,3,8,9]
val = int(input("Enter value to remove :"))
res = remove_element(nums,val)
print("Number of elements in array : ",nums)
print("Length of the array after removing the element : ",res)