class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Time: O(nlogK)
        countMap = {}
        res = []

        for i in range(len(barcodes)):
            if barcodes[i] in countMap:
                countMap[barcodes[i]] += 1
            else:
                countMap[barcodes[i]] = 1 
        # print(countMap)
            
        max_heap = [(-count, num) for num, count in countMap.items()]
        heapq.heapify(max_heap)

        prev_count, prev_num = 0, None

        while max_heap:
            count, num = heapq.heappop(max_heap)
        
            res.append(num)
        
            # -cnt 
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_num))
            
            # updating the count 
            prev_count, prev_num = count + 1, num

        if len(res) == len(barcodes):
            return res
