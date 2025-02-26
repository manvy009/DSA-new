class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        res, seenSet = -1, set()
        for element in range(len(edges)): 
            count, currNode = 0, element
            cycleMap = dict()
            while currNode not in seenSet and currNode != -1:
                count += 1
                seenSet.add(currNode); cycleMap[currNode] = count 
                currNode = edges[currNode] 
            res = max(res, count + 1 - cycleMap.get(currNode, 200000)) 
        return res