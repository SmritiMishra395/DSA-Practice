#BRUTE
def count_occurences(nums,target):
    n= len(nums)
    count = 0
    for i in range(0,n):
        if nums[i] == target:
            count += 1
    return count

nums= [1,2,3,3,3,3,3,5,6,8,9,9,10]
target= 3
print("The number of times: ", count_occurences(nums,target))

#BETTER
def count_occurence(nums,target):
    n= len(nums)
    first = -1
    last = -1
    for i in range(0,n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    if first == -1:
        return 0
    return last - first + 1
nums= [1,2,3,3,3,3,3,5,6,8,9,9,10]
target= 3
print("The number of times: ", count_occurences(nums,target))

#OPTIMAL
class Solution:
    def lower_bound(self,nums,target):
        n = len(nums)
        lb = -1
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb
    def upper_bound(self,nums,target):
        n= len(nums)
        ub = n
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub
    def countFreq(self, nums, target):
        
        lb = self.lower_bound(nums,target)
        if lb == -1:
            return 0
        ub = self.upper_bound(nums,target)
        return ub - lb
        
