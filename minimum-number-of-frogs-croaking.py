class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        count = Counter(croakOfFrogs)
        char_count = None
        for _, v in count.items():
            if not char_count:
                char_count = v
            elif v != char_count:
                return -1
        
        pos = {'c':0,'r':1,'o':2,'a':3,'k':4}
        maxFrog = 0
        frog = 0
        count = [0]*5
        for i in range(len(croakOfFrogs)):
            cur = croakOfFrogs[i]
            idx = pos[cur]
            
            if idx == 0:
                frog += 1
                maxFrog = max(maxFrog, frog)
            elif count[idx-1] == 0:
                return -1
            elif idx == 4:
                frog -= 1
            count[idx-1] -= 1
            count[idx] += 1
        
        return maxFrog if frog == 0 else -1
