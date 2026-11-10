class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        
        result = []
        for i in range(k):
            result.append(max(counts, key=counts.get)) # merken wie der aufruf gehT!
            del counts[max(counts, key=counts.get)]
        
        return result
