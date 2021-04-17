class SnapshotArray:

    def __init__(self, length: int):
        self.d = {}
        self.snap_d = {}
        self.snap_times = -1
        

    def set(self, index: int, val: int) -> None:
        self.d[index] = val

    def snap(self) -> int:
        self.snap_times += 1
        self.snap_d[self.snap_times] = self.d.copy()
        return self.snap_times
        

    def get(self, index: int, snap_id: int) -> int:
        d_at_snap = self.snap_d[snap_id]
        if index in d_at_snap:
            return d_at_snap[index]
        return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
