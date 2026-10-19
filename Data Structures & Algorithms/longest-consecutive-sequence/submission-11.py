class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums) 

        all_seq_lengths = []
        sub_seq_len = 1

        for i in nums_s: 
            if i - 1 not in nums_s:
                while (i+1) in nums_s: 
                    sub_seq_len += 1
                    i += 1
                all_seq_lengths.append(sub_seq_len)
                sub_seq_len = 1
        
        return max(all_seq_lengths, default=0)


        
        
            
        