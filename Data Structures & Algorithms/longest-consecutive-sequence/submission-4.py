class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # beispiel: 14589
        nums_s = set(nums) 
            # set erzeugt beliebige Reihenfolge!
        nums_s = sorted(nums_s)
            # sorted gibt immer eine Liste zurück!
        
        all_seq_lengths = []
        sub_seq =[]
        for i in nums_s: 
            sub_seq.append(i)
            while (i+1) in nums_s: 
                sub_seq.append(i+1)
                i += 1
            all_seq_lengths.append(len(sub_seq))
            sub_seq =[]
        
        return max(all_seq_lengths, default=0)


        
        
            
        