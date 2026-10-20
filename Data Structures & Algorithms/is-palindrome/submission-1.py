class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer_left = 0 
        pointer_right = len(s) - 1
        word_left = []
        word_right = []

        if len(s) > 0:
            word_left.append(s[pointer_left])
            word_right.append(s[pointer_right])
            if word_left != word_right:
                return False
            pointer_left +=1
            pointer_right -=1

    
        return True
            
        