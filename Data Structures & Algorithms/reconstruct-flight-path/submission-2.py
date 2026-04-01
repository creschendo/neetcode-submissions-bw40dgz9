class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # hierholzer's algorithm
        # guaranteed existence of an eulerian path, just need to return it

        # create adjacency list, sorted in reverse so that smaller lexical orders are
        # appended at the end of the list and will be processed first
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        # from starting node, traverse every neighbor, only appending 
        # when there are no neighbors left
        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
        
        # reverse the result at the end
        dfs('JFK')
        return res[::-1]