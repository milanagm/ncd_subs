class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False

        def create_dict(word): 
            dict_count ={}
            for letter in word: 
                dict_count[letter] = dict_count.get(letter, 0) +1
            return dict_count

        dict_count_s = create_dict(s)
        dict_count_t = create_dict(t)
            
        return dict_count_s == dict_count_t