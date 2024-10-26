class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.maxHeap = []
        for num in nums:
            heapq.heappush(self.maxHeap, -1 * num)
        heapq.heapify(self.maxHeap)

        for _ in range(k):
            kth_largest = -1 * heapq.heappop(self.maxHeap)
        return kth_largest