class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree cannot have more than n - 1 edges, or a cycle exists
        if len(edges) > (n - 1):
            return False

        # Create adjacency list, and add neighbors to both nodes
        # since the graph is undirected
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Check for cycles
        visit = set()
        def dfs(node, par):
            # If the node is already visited, a cycle exists
            if node in visit:
                return False

            # Add the node to set of visited nodes
            visit.add(node)

            # Check every neighbor for cycles
            for nei in adj[node]:
                # Ignore the edge back to the parent
                if nei == par:
                    continue
                # General case
                if not dfs(nei, node):
                    return False
            return True
            
        # Check if there are no cycles and the number of visited nodes
        # is equivalent to n, which means the graph is fully connected
        return dfs(0, -1) and len(visit) == n
