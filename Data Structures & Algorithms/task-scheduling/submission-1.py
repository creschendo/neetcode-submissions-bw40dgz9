class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(maxHeap)

        # queue stores pairs of count, cooldown
        time = 0
        queue = deque()

        while maxHeap or queue:
            time += 1
            if not maxHeap:
                time = queue[0][1]
            else:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    queue.append([count, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time