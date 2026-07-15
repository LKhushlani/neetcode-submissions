class SegmentTree:
    def __init__(self, N,A):
        self.n = 1
        while self.n < N:
            self.n*= 2
        self.build(N,A)

    def build(self,N,A):

        self.tree = [float("-infinity")] * 2 * self.n

        for i in range(N):
            self.tree[self.n+i] = A[i]
        
        for i in range(self.n-1,0,-1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])


    def query(self,l,r):

        l += self.n
        r += self.n+1
        res = -float("inf")

        while l < r:

            # if left is odd
            if l%2 == 1:
                res = max(self.tree[l], res)
                l += 1
            # if end is odd
            if r %2 == 1:
                r -= 1
                res = max(self.tree[r], res)
            
            l=l//2
            r = r//2

        return res      

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []
        n = len(nums)
        segTree = SegmentTree(n, nums)
        res = []

        for i in range(n-k+1):
            res.append(segTree.query(i, i+k-1))

        return res




        
        