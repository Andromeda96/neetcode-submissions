class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair = sorted(pair, reverse = True, key = lambda pa: pa[0])
        fleet = []
        t0 = 0
        for p, s in pair:
            time = (target - p)/s
            if time > t0:
                t0  = time
                fleet.append(time)
        
        return len(fleet)
        