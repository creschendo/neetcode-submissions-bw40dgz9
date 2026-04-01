class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Create adjacency list of all edges
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Traverse each component as deep as possible via BFS
        # Since graph is undirected, it doesn't matter which you
        # start at. Nonrecursive
        def bfs(node):
            # Add node to queue
            queue = deque([node])

            # Mark the node as visited
            visit[node] = True

            # While there are still neighbors
            while queue:

                # Add every neighbor to queue
                curr = queue.popleft()
                for neighbor in adj[curr]:

                    # If the neighbor hasn't been visited, set to True
                    if not visit[neighbor]:
                        visit[neighbor] = True

                        # Add neighbor to queue
                        queue.append(neighbor)
        
        sol = 0

        # Check every node
        for node in range(n):

            # If the current node isn't part of any previously
            # seen connected component, check it and add 1
            if not visit[node]:
                bfs(node)
                sol += 1

        return sol