from collections import defaultdict, deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph=defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        q=deque([0])
        vis=set([0])
        flips=0
        while q:
            node=q.popleft()
            for neighbor, direction in graph[node]:
                if neighbor not in vis:
                    vis.add(neighbor)
                    flips += direction
                    q.append(neighbor)
        return flips