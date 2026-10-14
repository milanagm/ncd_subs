class Solution:
    def topKFrequent (self, nums: List[int], k: int) -> List[int]: 
        map = defaultdict(int)
        for i in nums:
            map[i] +=1
        
        map_s = sorted(map.items(), key=lambda x:x[1], reverse = True)

        answer = []
        for j in range(k):
            answer.append(map_s[j][0])
        
        return answer


