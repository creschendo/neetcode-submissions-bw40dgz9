class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort intervals by start
        intervals.sort()

        # use a min heap to store (length, endpoint                
        minH = []

        # use a map to store lengths for each query, 
        # since we sort queries as well
        sol = {}

        i = 0
        for q in sorted(queries):
            # push every interval such that it starts before the current query
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minH, (r - l + 1, r))
                i += 1
            
            # remove every interval that ends before the query
            while minH and minH[0][1] < q:
                heapq.heappop(minH)
            
            # top interval is the shortest inclusive interval by definition
            sol[q] = minH[0][0] if minH else - 1

        # return solutions in original query order
        return [sol[q] for q in queries]

        """
        CORRECTNESS
        - sorting both the queries and intervals on start time
        ensures that for any query, after both loops have run, 
        the min heap contains only intervals such that the query is included, 
        and by definition, the top interval is the shortest

        - we don't worry about backtracking since we sort queries
            - Since queries are strictly non-decreasing, there can never 
            be an interval in the heap whose start time is after the current 
            query; any such interval hasn't been encountered yet and therefore 
            hasn't been added.

            - Similarly, once an interval is removed in the second loop because r < q, 
            it can never be valid for any future query. If an interval ends before the 
            current query, it must also end before all subsequent queries.

            - As a result, the heap always represents exactly the set of currently valid 
            intervals, and its top element is always the shortest valid interval for the 
            current query.

        """