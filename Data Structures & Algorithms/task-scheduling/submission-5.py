class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(maxHeap)
        # queue stores pairs of count, cooldown queue
        time = 0
        queue = deque()

        while maxHeap or queue:
            time += 1

            # if maxheap is empty, increment time to next cooldown time
            if not maxHeap:
                time = queue[0][1]

            # if maxheap isn't empty, remove most frequent and
            # add to queue with time it will be available again
            else:
                count = 1 + heapq.heappop(maxHeap)

                # if quota hasn't been met, add to queue
                if count:
                    queue.append([count, time + n])
            
            # if top element in queue is available at 
            # current time, add to maxheap
            if queue and queue[0][1] == time:
                # will be usable on next turn
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time