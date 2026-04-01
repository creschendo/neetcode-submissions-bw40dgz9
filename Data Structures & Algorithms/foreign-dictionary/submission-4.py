class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Create an adjacency list for every word in the list
        adj = {c: set() for w in words for c in w}

        # Compare each pair of words, stopping at the first 
        # differing letter. 
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen =min(len(w1), len(w2))
            # If the word 1 is longer and the first minLen letter are the same, 
            # there is no valid solution
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return""

            # Add the first differing letter to word1's adjacency list
            # Indicating that the first differing letter in word 2 comes after
            # that in word 1
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
            
        
        # Create a visited map
        #   - Present false means that node has been seen before but
        #     not in current path
        #   - Present true means that node has been seen and is in the
        #     current path, indicating a cycle, so invalid solution
        visited = {}
        res = []

        # Traverse each letter via dfs
        def dfs(char):
            # Return whether the char has been visited in a previous pass
            # or if it was visited in the current pass, indicating a cycle
            if char in visited:
                return visited[char]
            
            # Set the char to visited in this pass
            visited[char] = True
            
            # Check each neighbor
            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True

            # Set char to false
            visited[char] = False

            # Add to result
            res.append(char)

        # Run dfs on each letter
        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)