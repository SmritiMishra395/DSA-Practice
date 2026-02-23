#BRUTE
def fun(arr,target):
    n= len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                return [i,j]
            
    return -1


#OPTIMAL
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i
