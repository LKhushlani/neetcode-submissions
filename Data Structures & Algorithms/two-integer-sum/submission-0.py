class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = {}

        for i,num in enumerate(nums):
            diff = target-num
            if diff not in res:
                res[num] = i
            else:
                return [res[diff],i]

            
                

            
        