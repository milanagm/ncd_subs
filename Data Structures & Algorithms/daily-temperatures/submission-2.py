class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i, v in enumerate(temperatures): 
            for j in range(i+1, len(temperatures)):  
                if temperatures[j] > v: 
                    result.append(j-i)
                    break
            else: 
                result.append(0) 
        return result