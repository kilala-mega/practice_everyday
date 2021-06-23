class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        intersection = []
        p1, p2 = 0, 0
        n1, n2 = len(firstList), len(secondList)
        
        while p1 < n1 and p2 < n2:
            start1, end1 = firstList[p1][0], firstList[p1][1]
            start2, end2 = secondList[p2][0], secondList[p2][1]
            if end1 < end2:
                if start2 <= end1:
                    intersection.append([max(start1, start2), end1])
                p1 += 1
            else:
                if start1 <= end2:
                    intersection.append([max(start1, start2), end2])
                p2 += 1
        return intersection
            
        
