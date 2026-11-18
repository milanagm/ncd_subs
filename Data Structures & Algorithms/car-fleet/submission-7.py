class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  
        fleets = 0
        slowest = 0  # arrival time of the fleet directly ahead
        for p, s in cars:
            t = (target - p) / s
            if t > slowest:      # can't catch the fleet ahead → new fleet
                fleets += 1
                slowest = t
        return fleets
        
        
        