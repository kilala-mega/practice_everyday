class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        counts = [0] * n
        
        numsWithIndex = list(enumerate(nums))
        def mergeSort(start, end, numsWithIndex):
            if start >= end:
                return
            mid = (start + end)//2
            mergeSort(start, mid, numsWithIndex)
            mergeSort(mid+1, end, numsWithIndex)

            mergedNums = []

            l, r = start, mid+1
            numElemsRightArrayLessThanLeftArray = 0
            while l <= mid and r <= end:
                if numsWithIndex[l][1] > numsWithIndex[r][1]:
                    numElemsRightArrayLessThanLeftArray += 1
                    mergedNums.append(numsWithIndex[r])
                    r += 1
                else:
                    counts[numsWithIndex[l][0]] += numElemsRightArrayLessThanLeftArray
                    mergedNums.append(numsWithIndex[l])
                    l+= 1
            while l <= mid:
                counts[numsWithIndex[l][0]] += numElemsRightArrayLessThanLeftArray
                mergedNums.append(numsWithIndex[l])
                l+= 1
            while r <= end:
                mergedNums.append(numsWithIndex[r])
                r += 1
            pos = start
            for m in mergedNums:
                numsWithIndex[pos] = m
                pos += 1
            
        mergeSort(0, n-1, numsWithIndex)
        
        return counts
        

        
