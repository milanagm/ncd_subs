class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums: 
            if i in counts:
                counts[i] += 1
            else: 
                counts[i] = 1
        
        result = []
        while i < k:
            result.append(max(counts, key = counts.get))
            del counts[max(counts, key = counts.get)]
            i += 1
        
        return result
            
            

        