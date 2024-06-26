class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.maxheap = []
        # Time complexity: O(n)
        for num in nums:
            heapq.heappush(self.maxheap, -1 * num)
        heapq.heapify(self.maxheap)

        # print(self.maxheap)
        # val = -1 * self.maxheap[k-1]
        for _ in range(k):
            kth_largest = -heapq.heappop(self.maxheap)  # Negate the result to get the actual value
        return kth_largest
       