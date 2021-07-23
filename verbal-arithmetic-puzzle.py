"""

"""
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        words.append(result)
        R, C = len(words), max(map(len, words))
        # search list of words from right to left, top to bottom
        
        assigned = {} # {letters: d}
        assigned_inv = [None] * 10 # i: letter

        def search(column, row, bal):
            if column >= C: 
                # end of all columns
                return bal == 0
            if row == R: 
                # end of one column
                return bal % 10 == 0 and search(column + 1, 0, bal // 10)
            
            word = words[row] # word/result at row-th row
            if column >= len(word): 
                # finish current word, search next word 
                return search(column, row + 1, bal)
            
            letter = word[~column] # use ~ to traverse list backwards
            sign = 1 if row < R - 1 else -1 # sum(words) - result
            if letter in assigned:
                # add the digit and check next word at the same column
                if (assigned[letter] > 0 or len(word) == 1 or column != len(word) - 1):
                    return search(column, row + 1, bal + sign * assigned[letter])
                return False
            else:
                for d, ad in enumerate(assigned_inv):
                    if ad is None and (d > 0 or column != len(word) - 1): # d >0 or not the first column
                        assigned_inv[d] = letter
                        assigned[letter] = d
                        if search(column, row + 1, bal + sign * d):
                            return True
                        assigned_inv[d] = None
                        del assigned[letter]
            
            return False
        
        return search(0, 0, 0)
        
        
