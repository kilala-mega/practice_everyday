class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(",")
        slots = 1
        for n in nodes:
            slots -= 1
            if slots < 0:
                return False
            if n != "#":
                slots += 2
        return slots == 0
