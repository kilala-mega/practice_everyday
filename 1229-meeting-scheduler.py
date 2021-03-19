class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        # For each person meeting schedule doesn't overlap 
        # return earliest time slot works for both, if can't find, return []
        # is the slots1/slots2 sorted by meeting beginning time?
        if slots1 is None or slots2 is None or len(slots1) == 0 or len(slots2)==0:
            return []
        # sort, don't use sorted() 
        slots1.sort()
        slots2.sort()
        # two pointers search
        p1, p2 = 0, 0
        while p1 < len(slots1) and p2 < len(slots2):
            begin1, end1, begin2, end2 = slots1[p1][0], slots1[p1][1], slots2[p2][0], slots2[p2][1]
            begin = max(begin1, begin2)
            end = min(end1, end2)
            if end-begin>=duration:
                return [begin, begin+duration]
            if end1 < end2:
                p1+=1
            else:
                p2+=1
        return []
