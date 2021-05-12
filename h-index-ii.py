class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        start, end = 0, len(citations)-1
        
        while start + 1 < end:
            mid = (start + end) //2
            citation = citations[mid]
            if len(citations)-mid >= citation:
                start = mid
            else:
                end = mid
        
        endCitation = min(citations[end], len(citations)-end)
        startCitation = min(citations[start], len(citations)-start)
        return max(startCitation, endCitation)
        
