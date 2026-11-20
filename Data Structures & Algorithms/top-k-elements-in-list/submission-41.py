class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0)+1
        
        maxk = []
        for i in range(k):
            m = max(counter, key= counter.get)
            maxk.append(m)
            del counter[m]
        
        return maxk


