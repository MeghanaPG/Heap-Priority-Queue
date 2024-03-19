class MedianFinder:
    # add/remove an element from the heap is O(logn) time complexity 
    # To get the median we want the max value from the small heap whcih is max heap and small value from the max heap which takes O(1) time. 

    def __init__(self):
    # two heaps, large and small -> minHeap and maxHeap respectively 
    # heaps should be equal size 
    # Max heap and then min heap
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        # -1 because python doesn't allow max heap implementation 
        heapq.heappush(self.small, -1 * num)

        # make sure every num in small is <= every num in large 
        if(self.small and self.large and 
        ( -1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size? 
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0])/2 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()