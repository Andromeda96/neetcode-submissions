class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        results = []
        for i in range(l-1):
            cur_temp = temperatures[i]
            for j in range(i+1, l):
                future_temp = temperatures[j]
                if future_temp > cur_temp:
                    results.append(j  - i)
                    break
                if j == l-1:
                    results.append(0)


            
        results.append(0)
        return results
