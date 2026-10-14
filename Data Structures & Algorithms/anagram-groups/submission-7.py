class Solution:
    def groupAnagrams (self, strs: List[str]) -> List[List[str]]:
        maper = {}
        answer = []

        for s in strs: 
            s_s = "".join(sorted(s))
            if s_s in maper: 
                idx = maper[s_s]
                answer[idx].append(s)
            else: 
                maper[s_s] = len(answer)
                answer.append([s])
        
        return answer
                
