class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        
        stack = [] # (idx, val)
        res = [0] * len(t) 

        for idx, val in enumerate(t):

            while stack and val > stack[-1][1]:
                s_idx, s_val = stack.pop()
                res[s_idx] = idx- s_idx

            stack.append((idx,val))

        return res 