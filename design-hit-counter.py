class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits_per_sec = {}
        self.seconds = deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # hit will be heavily called compared to getHits, we do the cleanup in getHits
        if timestamp in self.hits_per_sec:
            self.hits_per_sec[timestamp] += 1
        else:
            self.hits_per_sec[timestamp] = 1
            self.seconds.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while len(self.seconds) > 0 and timestamp - 300 >= self.seconds[0]:
            expired = self.seconds.popleft()
            del self.hits_per_sec[expired]
        count = 0
        for _, v in self.hits_per_sec.items():
            count += v
        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
