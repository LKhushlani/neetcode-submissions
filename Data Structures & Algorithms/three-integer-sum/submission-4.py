class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lp = i+1
            rp = len(nums) - 1
            
            while lp < rp:
                tsum = nums[i] + nums[lp] + nums[rp]
                if tsum == 0:
                    res.append([nums[i], nums[lp], nums[rp]])                    
                    lp+=1
                    rp -=1
                    while lp < rp and nums[lp] == nums[lp-1]:
                        lp+=1                        
                elif tsum >0:
                    rp -=1
                else:
                    lp += 1

        return res

