class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        def findMinCost(cneededTime):
            cneededTime.remove(max(cneededTime))
            return sum(cneededTime)
        
        curConList = []
        curCost = 0
        curColor = ""
        for i in range(0, len(colors)):
            currentColor = colors[i]
            if curColor == currentColor:
                curConList.append(i)
            else:
                if len(curConList) > 1:
                    curCost += findMinCost(neededTime[curConList[0]:curConList[-1] + 1])
                curConList = [i]
                curColor = currentColor
        if len(curConList) > 1:
            curCost += findMinCost(neededTime[curConList[0]:curConList[-1] + 1])
        return curCost
            
        
"""
aaa
[1, 3, 1]

[a,a,a,b,b,a,a,a]
[1,2,2,3,3,4,1,1]
   2   3     1
[a   a b   a   a]
"""