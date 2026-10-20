class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = set()
        for i, v in enumerate(numbers): 
            diff = target - v 
            if diff in seen: 
                return [numbers.get_index(diff)+1, i+1 ]
            seen.add(v)

