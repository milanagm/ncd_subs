class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        dictionary = {}
        answer=[]
        counter = 0
        for word in words:
            key = "".join(sorted(word))
            if key in dictionary:
                idx = dictionary[key]
                answer[idx].append(word)
            else: 
                dictionary[key] = counter
                answer.append( [word] )
                counter += 1
        
        return answer
