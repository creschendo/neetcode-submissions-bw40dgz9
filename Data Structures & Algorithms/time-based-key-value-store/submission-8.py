class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # list of values and timestamps for specific key
        vals = self.timemap.get(key)
        if not vals:
            return ""

        # binary search to find greatest value less than or equal to 
        # desired timestamp
        left, right = 0, len(vals) - 1
        sol = None
        while left <= right:
            mid = (left + right) // 2
            if vals[mid][1] > timestamp:
                right = mid - 1
            elif vals[mid][1] < timestamp:
                # if mid is less, its a potential condidate
                # we go right after, so every value after is 
                # strictly greater and max() isn't necessary
                sol = mid
                left = mid + 1
            else:
                # direct timestamp match, just set sol and break
                sol = mid
                break
        # we've found either a valid timestamp
        if sol != None:
            return vals[sol][0]
        
        # no valid timestamp found
        else:
            return ""
