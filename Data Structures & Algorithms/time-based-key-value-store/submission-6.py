class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.timeMap.get(key)
        if not vals:
            return ""
        left, right = 0, len(vals) - 1
        maxt = float('-inf')
        val = ""
        while left <= right:
            mid = (left + right) // 2
            if vals[mid][1] > timestamp:
                right = mid - 1
            elif vals[mid][1] < timestamp:
                maxt = max(maxt, vals[mid][1])
                val = vals[mid][0]
                left = mid + 1
            else:
                return vals[mid][0]
        return val
        