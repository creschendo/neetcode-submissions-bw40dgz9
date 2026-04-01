class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # add indices onto task lists, making triples of 
        # [enqueue time, process time, index]
        for i, t in enumerate(tasks):
            t.append(i)

        # sort the tasks based on enqueue time
        tasks.sort(key=lambda t: t[0])
        
        sol, minHeap = [], []

        # initialize to first index, first time
        i, time = 0, tasks[0][0]

        while minHeap or i < len(tasks):

            # add [processTime, index] of all tasks that are valid at the time
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1

            # if no tasks were added, jump the time forward to the next
            # enqueue time
            if not minHeap:
                time = tasks[i][0]

            # pop the pair with the smallest procTime,
            # add it to solution, and jump time forward
            else:
                procTime, index = heapq.heappop(minHeap)
                time += procTime
                print(time)
                sol.append(index)

        return sol