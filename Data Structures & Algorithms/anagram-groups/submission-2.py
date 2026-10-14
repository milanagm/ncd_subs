class Solution:
    def groupAnagrams (self, strs: List[str]) -> List[List[str]]:
        indexer = {}
        answer = []
        nxt_empty = 0

        for word in strs: 
            word_sorted = "".join(sorted(word))
            if word_sorted in indexer: 
                idx_append = indexer[word_sorted]
                answer[idx_append].append(word)
            else: 
                indexer[word_sorted] = nxt_empty
                answer.append([word])
                nxt_empty +=1
        return answer