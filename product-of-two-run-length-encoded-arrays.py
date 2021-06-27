class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        encoded_prodnums = []
        index1, index2 = 0, 0
        
        while index1 < len(encoded1) and index2 < len(encoded2):
            val1, freq1 = encoded1[index1]
            val2, freq2 = encoded2[index2]
            
            product = val1*val2
            freq = min(freq1, freq2)
            
            encoded1[index1][1] -= freq
            encoded2[index2][1] -= freq
            
            if encoded1[index1][1] == 0:
                index1 += 1
            
            if encoded2[index2][1] == 0:
                index2 += 1
            
            if encoded_prodnums and encoded_prodnums[-1][0] == product:
                encoded_prodnums[-1][1] += freq
            else:
                encoded_prodnums.append([product, freq])
        return encoded_prodnums
