class TimeMap:

    def __init__(self):
        self.timemap = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((value, timestamp))
    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap.get(key, [])
        if not values:
            return ''
        l = 0
        r = len(values) - 1
        while l <= r:
            m = (l + r) //2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] > timestamp:
                r = m - 1
            elif values[m][1] < timestamp:
                l = m + 1
        
        return values[r][0] if r >= 0 else ""


