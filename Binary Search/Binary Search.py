#ITERATIVE SOLUTION
def binarySearch(nums,target):
    n= len(nums)
    low= 0
    high= n-1
    while low <= high:
        mid= (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid-1
        else:
            low = mid + 1
    return -1

#Example
nums= [2,4,6,7,9,11,18,19]
target= 6
print(f"The {target} is at ",binarySearch(nums,target))

#RECURSIVE SOLUTION
def binarySearch(nums,target,low,high):
    mid = (low + high)//2
    if low > high:
        return -1
    elif nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binarySearch(nums,target,low,mid-1)
    else:
        return binarySearch(nums,target,mid+1,high)
##Example
nums= [2,4,6,7,9,11,18,19]
target= 6
print(f"The {target} is at ",binarySearch(nums,target,0,len(nums)))
