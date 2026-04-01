class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # minimum spanning tree problem
        # prim's algorithm

        # create an adjacency list for every pair of points
        # for points i and j, append distance between them to 
        # adj[i] and adj[j]
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        minH = [[0, 0]]

        # use a minHeap to greedily choose the next 
        # cheapest path to connect the next node
        while len(visit) < N:
            # pop next cheapest point to connect to
            cost, i = heapq.heappop(minH)

            # if we've already visited, skip
            if i in visit:
                continue

            # add to total cost
            res += cost

            # mark visited
            visit.add(i)

            # add each neighbor and their distances, if not visited
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])

        return res