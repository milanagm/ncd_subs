class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(k):
            counts.append(max(nums.get_values))
        return counts
