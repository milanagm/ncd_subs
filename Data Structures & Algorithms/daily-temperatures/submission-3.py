class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        waiting = []  

        for i, v in enumerate(temperatures):
            while waiting and v > temperatures[waiting[-1]]:
                j = waiting.pop()
                result[j] = i - j
            waiting.append(i)

        return result