class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones  = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))

            print(first, second)

            if first > second: 
                heapq.heappush(stones,-(first-second))

            print(stones)
        stones.append(0)
        return abs(stones[0])

            

        

