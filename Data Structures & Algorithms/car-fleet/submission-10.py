class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        new_p = position
        fleets = 0
        seen_speed = set()

        cars = n - 1 
        while cars > 0:
            for i in range(len(position)): 
                if i < n - 1:
                    new_p[i] = min(new_p[i]+speed[i], new_p[i+1])
                    #print(new_p[i]) # 4 # 6 # 8
                else: 
                    new_p[i] += speed[i]
                    #print(new_p[i]) # 6 # 8 # 10
                    
                if new_p[i] >= target: 
                    cars -= 1
                    if new_p[i] not in seen_speed: 
                        fleets += 1
                        
                
        return fleets
    