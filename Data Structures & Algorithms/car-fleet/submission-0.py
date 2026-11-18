class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #1,4 #4,6 #7,8 #10,10

        fleets = 0
        current = position
        remove = []

        while len(position) > 0:
            for i in range(position): 
                new_p = min(position[i] + speed[i], position[-1] + speed[-1])
                position[i] = new_p
                if position[i] >= target:
                    remove.append(i)

            if len(remove) > 0:
                fleets += 1

            for i in remove: 
                del position[i]
                del speed[i]
            
            remove = []

        return fleets
        
        
        
        