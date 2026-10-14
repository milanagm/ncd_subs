class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}

        for string in strs: 
            key = "".join(sorted(string))

            if key in result:
                result[key].append(string)
            
            else: 
                result[key] = [string]

        
        return list(result.values())