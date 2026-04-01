class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Create adjacency list of all edges
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            queue = deque([node])
            visit[node] = True
            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if not visit[neighbor]:
                        visit[neighbor] = True
                        queue.append(neighbor)
        
        sol = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                sol += 1

        return sol