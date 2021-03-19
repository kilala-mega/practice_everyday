class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        # a list of x
        # find maxheight in x = (i,j)
        # problem of merging intervals and meeting romms 
        events = {}
        for x1, y1, x2, y2 in rectangles:
            events.setdefault(y1, []).append((1, x1, x2))
            events.setdefault(y2, []).append((0, x1, x2))
        events = sorted(events.items(), key=lambda x:x[0])  
        area = 0
        width = 0
        intervals = []
        lasty = events[0][0]
        
        for y,event in events:
            area += (y - lasty)*width
            for start, x1, x2 in event:
                if start:
                    intervals.append([x1, x2])
                else:
                    intervals.remove([x1, x2])
            width = self.merge(intervals)
            lasty = y
        return area % (10**9 + 7)
    
    def merge(self, intervals):
        if not intervals:
            return 0
        intervals.sort()
        ans = intervals[0][1] - intervals[0][0]
        end = intervals[0][1]
        for l,r in intervals:
            if l >= end:
                ans += r-l
                end = r
            if l < end and end < r:
                ans += r - end
                end = r
                
        return ans
