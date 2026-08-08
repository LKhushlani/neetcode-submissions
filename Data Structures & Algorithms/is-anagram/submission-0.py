class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = collections.defaultdict()
        d2 = collections.defaultdict()


        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            d1[c1] = 1+ d1.get(c1,0)
            d2[c2] = 1+ d2.get(c2,0)

        return d1 == d2