class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]

        if not arr:
            return ""
        
        best = float('-inf')

        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2

            if arr[mid][1] <= timestamp:
                best = max(best, mid)
                left = mid + 1
            else:
                right = mid - 1
        if best == float('-inf'):
            return ""
        return arr[best][0]
