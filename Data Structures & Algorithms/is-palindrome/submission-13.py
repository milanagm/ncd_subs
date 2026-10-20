class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer_left = 0 
        pointer_right = len(s) - 1
        s = s.lower()

        if len(s) > 0:
            while pointer_left < pointer_right:
                while pointer_left < pointer_right and not s[pointer_left].isalnum():
                    pointer_left += 1
                while pointer_left < pointer_right and not s[pointer_right].isalnum():
                    pointer_right -= 1
                    
                if s[pointer_left] != s[pointer_right]:
                    return False

                pointer_left +=1
                pointer_right -=1

    
        return True
            
        