#BRUTE
def ceil_floor(nums,target):
    n= len(nums)
    floor = -1
    ceil = -1
    for i in range(0,n):
        if target in nums:
            floor = target
            ceil = target
        else:
            if nums[i] <= target:
                floor = nums[i]
            if nums[i] >= target:
                if ceil == -1 or nums[i] < ceil:
                    ceil = nums[i]
    return [floor,ceil]

#Example
nums= [3,4,4,4,8,9,9,10,12,12,14,15]
target= 11
print(f"The floor and ceil respectively of {target} are: ", ceil_floor(nums,target))

#OPTIMAL SOLUTION
def ceil_floor(nums,target):
    n = len(nums)
    floor = -1
    ceil = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return [nums[mid],nums[mid]]
        elif nums[mid] > target:
            ceil = nums[mid]
            high = mid - 1
        else:
            floor = nums[mid]
            low = mid + 1
    return [floor, ceil]
    
nums= [3,4,4,4,8,9,9,10,12,12,14,15]
target= 6
print(f"The floor and ceil respectively of {target} are: ", ceil_floor(nums,target))

