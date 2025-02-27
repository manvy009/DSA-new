class Solution:


    def dfs(self,preList,node,vis):
        if vis[node]==1:
            return True
        if vis[node]==2:
            return False
        vis[node]=1
        for neighbour in preList[node]:
            if self.dfs(preList,neighbour,vis):
                return True
        vis[node]=2
        return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preList=[[] for _ in range(numCourses)]
        for c,preq in prerequisites:
            preList[c].append(preq)
        vis=[0]*numCourses
        for i in range(numCourses):
            if vis[i]==0 and self.dfs(preList,i,vis):
                return False
        return True