class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = {}

        for number in nums: 
            result[number] = result.get(number , 0) +1

        sorted_keys = sorted(result, key=result.get, reverse=True)

        return sorted_keys[:k]