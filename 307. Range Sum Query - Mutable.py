class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.total = 0
        
class NumArray:
    def __init__(self, nums: List[int]):
        def _createSegTree(nums, l, r):
            if l > r:
                return None
            if l == r: # leaf node
                node = Node(l,r)
                node.total = nums[l]
                return node
            mid = (l+r)//2
            root = Node(l,r)
            root.left = _createSegTree(nums, l, mid)
            root.right = _createSegTree(nums, mid+1, r)
            root.total = root.left.total + root.right.total
            return root
        self.root = _createSegTree(nums, 0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        def _update(node):
            if not node:
                return
            if node.start == node.end:
                node.total = val
                return val
            mid = (node.start + node.end)//2
            if index <= mid:
                _update(node.left)
            else:
                _update(node.right)
            node.total = node.left.total + node.right.total
                
        _update(self.root)

    def sumRange(self, left: int, right: int) -> int:
        def _subRangeQuery(l, r, node):
            if not node:
                return 0
            if l == node.start and r == node.end:
                return node.total
            mid = (node.start + node.end)//2
            if r <= mid:
                return _subRangeQuery(l, r, node.left)
            elif l >= mid + 1:
                return _subRangeQuery(l, r, node.right)
            else:
                return _subRangeQuery(l, mid, node.left) + _subRangeQuery(mid+1, r, node.right)
        return _subRangeQuery(left, right, self.root)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
