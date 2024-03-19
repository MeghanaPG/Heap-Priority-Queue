class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with k largest integers
        self.minHeap, self.k = nums, k 
        # create the min Heap 
        heapq.heapify(self.minHeap)
        # We pop because we don't want more than k elemnents 
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        # we only want to pop if the length of the heap is greater than k 
        if len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap)
        # Now we have to return the min element and the way these heaps are implemennted the minval will always be stored in the 0th Index of the 
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)