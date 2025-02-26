from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        for c, pre in prerequisites:
            g[pre].append(c)
        in_degree=[0]*numCourses
        for c,pre in prerequisites:
            in_degree[c]+=1
        q=deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                q.append(i)
        
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for neighbour in g[node]:
                in_degree[neighbour]-=1
                if in_degree[neighbour]==0:
                    q.append(neighbour)
        if len(res)<numCourses:
            return []
        return res
