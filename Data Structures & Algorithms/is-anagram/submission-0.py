class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False

        dict_count_s = {} 
        
        for letter in s:
            dict_count_s[letter] = dict_count_s.get(letter, 0) +1 

        dict_count_t = {} 
        
        for letter in s:
            dict_count_t[letter] = dict_count_t.get(letter, 0) +1 
            
            
        return dict_count_s == dict_count_t