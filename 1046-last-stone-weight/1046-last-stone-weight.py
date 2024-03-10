class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        # heapify is a linear time operation 
        heapq.heapify(stones)

        while len(stones) > 1:
            # we are gonna take the two largest stones 
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                # first = -8, second = -7
                heapq.heappush(stones, first - second)
        # this is if the stones is empty 
        stones.append(0)
        return abs(stones[0])