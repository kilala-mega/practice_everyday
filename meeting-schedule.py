class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        if not slots1 or not slots2:
            return []
        
        slots1.sort()
        slots2.sort()
        
        slots = {}
        slots[1] = slots1
        slots[2] = slots2
        
        h = []
        heappush(h, (slots1[0][0], slots1[0][1], 1, 0))
        heappush(h, (slots2[0][0], slots2[0][1], 2, 0))
        while h and len(h) >= 2:
            start, end, person, index = heappop(h)
            next_start, next_end, next_person, next_index = h[0]
            if end > next_start and min(end, next_end) - next_start >= duration:
                    return [next_start, next_start + duration]
            if end > next_end:
                heappush(h, (next_end,end, person, index))
            elif index + 1 < len(slots[person]):
                heappush(h, (slots[person][index+1][0],slots[person][index+1][1], person, index+1))
        return []
                
            
        
        
