class Solution:   
    def pathSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nodes = {x//10:x%10 for x in nums}
        total = 0
        def search(nodeid: int, currSum: int) -> None:
            nonlocal total
            if nodeid not in nodes:
                return
            depth, pos, val = nodeid//10, nodeid%10, nodes[nodeid]
            currSum += val
            leftid = (depth+1)*10+(2*pos-1)
            rightid = leftid + 1
            if leftid not in nodes and rightid not in nodes:
                # it's a leaf node
                total += currSum
            else:
                search(leftid, currSum)
                search(rightid, currSum)
        search(nums[0]//10, 0)
        return total
