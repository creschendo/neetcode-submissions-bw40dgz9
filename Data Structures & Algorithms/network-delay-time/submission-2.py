class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # find shortest path to every other node
        # djikstra's algorithm

        # create a list of edges for each source to each destination, with cost to go there
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        # create a minHeap to track the next cheapest edge to pursue
        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            # pop the cheapest edge
            w1, n1 = heapq.heappop(minHeap)

            # if we've already been to the destination, skip
            if n1 in visit:
                continue

            # mark as visited
            visit.add(n1)

            # update time, w1 will be the aggregate time
            t = w1

            # add each neighbor and the cost to go there to the minHeap, added to current time
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
            
        return t if len(visit) == n else -1