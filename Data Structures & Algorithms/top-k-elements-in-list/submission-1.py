class Solution:
    def topKFrequent (self, nums: List[int], k: int) -> List[int]: 
        counter = {}
        answer = []

        for i in nums: 
            if i in counter:
                counter[i] +=1
            else: 
                counter[i] = 1

        s_counter = sorted(counter, key = lambda x:counter[x], reverse = True)
        
        for i in range(k): 
            answer.append(s_counter[i])

        return answer