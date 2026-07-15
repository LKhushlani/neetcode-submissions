from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1Count = defaultdict(int)
        s2Count = defaultdict(int)

        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1
        
        def matches():
            return s1Count == s2Count
        
        for r in range(len(s1), len(s2)):

            if matches():
                return True
            
            #add next item in window 
            s2Count[s2[r]] += 1

            #remove old item
            s2Count[s2[r-len(s1)]] -= 1
            
            # del unused item
            if s2Count[s2[r-len(s1)]] == 0:
                del s2Count[s2[r-len(s1)]]

        return matches()
            
        