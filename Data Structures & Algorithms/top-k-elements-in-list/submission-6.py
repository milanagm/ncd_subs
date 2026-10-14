class Solution:
    def topKFrequent (self, nums: List[int], k: int) -> List[int]: 
        map = defaultdict(int)

        for i in nums: 
            map[i] +=1
        
        s_map = sorted(map.items(), key = lambda x: x[1], reverse = True)

        answer = []
        for i in range(k):
            answer.append(s_map[i][0])
        
        return answer

        