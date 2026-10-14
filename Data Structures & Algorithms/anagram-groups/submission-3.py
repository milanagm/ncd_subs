class Solution:
    def groupAnagrams (self, strs: List[str]) -> List[List[str]]:
        indexer = {}
        answer = []
        idx = 0

        for word in strs: 
            s_w = "".join(sorted(word))
            if s_w in indexer: 
                find_idx = indexer[s_w]
                answer[find_idx].append(word)
            else: 
                indexer[s_w] = idx
                answer.append([word])
                idx +=1
        return answer

