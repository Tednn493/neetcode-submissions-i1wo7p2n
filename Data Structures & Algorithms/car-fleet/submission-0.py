class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr=[]
        for i in range (len(position)):
            arr.append([position[i],speed[i]])
        arr.sort(key=lambda x: -x[0])

        times = []
        for val in arr:
            time = (target - val[0]) / val[1]
            times.append(time)

        
        prevtime=times[0]
        res=1
        for i in range(1,len(times)):
            if times[i]>prevtime:
                prevtime = times[i]
                res+=1
        return res
            

        


        