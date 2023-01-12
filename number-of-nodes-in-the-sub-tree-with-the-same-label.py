class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        retList = [1] * n
        graph = {}
        labelCounts = {}

        for a, b in edges:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]

            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]
        
        retList = self.dfs(n, labels, graph, labelCounts, retList)

        return retList



    def dfs(self, n, labels, graph, labelCounts, retList, node = 0, parent = None):
        old = 0
        if labels[node] in labelCounts:
            old = labelCounts[labels[node]]
            labelCounts[labels[node]] += 1
        else:
            labelCounts[labels[node]] = 1

        for child in graph[node]:
            if child != parent:
                retList = self.dfs(n, labels, graph, labelCounts, retList, child, node)

        retList[node] = labelCounts[labels[node]] - old
        return retList