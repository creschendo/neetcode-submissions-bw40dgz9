class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap.setdefault(key, []).append((value, timestamp))
        print(self.timemap)

    def get(self, key: str, timestamp: int) -> str:
        vals = self.timemap.get(key)
        if not vals:
            return ""
        left, right = 0, len(vals) - 1
        sol = None
        while left <= right:
            mid = (left + right) // 2
            print("timestamp:" + str(timestamp))
            print(vals[mid])
            if vals[mid][1] > timestamp:
                right = mid - 1
            elif vals[mid][1] < timestamp:
                sol = mid
                left = mid + 1
            else:
                print("equal")
                sol = mid
                break
        if sol != None:
            return vals[sol][0]
        else:
            return ""
