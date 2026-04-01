class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []

        # count occurrences
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            # pop highest count
            count, char = heapq.heappop(maxHeap)

            # if last two characters are same as current
            if len(res) > 1 and res[-1] == res[-2] == char:

                # nothing left in heap, break
                # longest solution found
                if not maxHeap:
                    break

                # get next largest count char, use it instead
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1

                # add back second
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))

                # add back first
                heapq.heappush(maxHeap, (count, char))
            else:
                # use current, push back
                res += char
                count += 1
                if count:
                    heapq.heappush(maxHeap, (count, char))
        
        return res