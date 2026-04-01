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

    # [[1,4],[3,3],[2,1]]
    # [[1,4,0],[3,3,1],[2,1,2]]
    # [[1,4,0],[2,1,2],[3,3,1]]
    # i = 0, time = 1

    # minHeap = [4,0]
    # time = 5
    # sol = [0]
    
    # i = 1, time = 5
    # minHeap = [[1, 2], [3, 1]]
    # time = 6
    # sol = [0, 2]
    # time = 9
    # sol = [0, 2, 1]
    