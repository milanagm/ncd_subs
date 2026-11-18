class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        position = sorted(position)
        speed = sorted(speed)
        remove = []
        while len(position) > 0:
            for i in range(len(position)): 
                new_p = min(position[i] + speed[i], position[i+1] + speed[i+1])
                position[i] = new_p
                if position[i] >= target:
                    remove.append(i)

            if len(remove) > 0:
                fleets += 1

            for i in reversed(remove): #how can I delete in reverse order?
                del position[i]
                del speed[i]
            
            remove = []

        return fleets
        
        
        
        