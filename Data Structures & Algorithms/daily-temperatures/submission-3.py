class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res= [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            if not s:
                s.append([i,t])
            else:
                while s and s[-1][1]<temperatures[i]:
                    tempI = s.pop()[0]
                    res[tempI]= i - tempI
                s.append([i,t])
        return res
        