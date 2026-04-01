class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        best = float('inf')
        sol = [-1, -1]
        counts = {}
        for char in t:
            counts[char] = counts.get(char, 0) + 1
        need = len(counts)

        left = 0 
        have = 0
        window = defaultdict(int) 
        for right in range(len(s)):
            window[s[right]] += 1

            if s[right] in counts and window[s[right]] == counts[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < best:
                    best = right - left + 1
                    sol = [left, right]

                window[s[left]] -= 1

                if s[left] in counts and window[s[left]] < counts[s[left]]:
                    have -= 1
                
                left += 1
        
        return s[sol[0]:sol[1] + 1] if best != float('inf') else ""

