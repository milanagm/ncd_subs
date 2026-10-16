class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums: 
            counter[n] += 1
        
        s_counter = sorted(conter.items(), key = lambda x: x[1], reverse= True )

        answer = []
        for i in enumerate(k):
            answer.append(s_counter.index(i))

        return answer





        