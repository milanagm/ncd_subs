class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # anlegen von arrays einer bestimmten länge vergesse ich immer
        waiting = []  

        for i, v in enumerate(temperatures):
            while waiting and v > temperatures[waiting[-1]]:
                j = waiting.pop()
                result[j] = i - j
            waiting.append(i)

        return result