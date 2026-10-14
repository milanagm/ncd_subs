class Solution:
    def groupAnagrams (self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        answer = []

        for s in strs: 
            s_s = "".join(sorted(s))
            map[s_s].append(s)

        answer = list(map.values())
        
        return answer
                
