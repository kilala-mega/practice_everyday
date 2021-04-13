import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos = {}
        self.val = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False
        self.pos[val] = len(self.val)
        self.val.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos:
            return False
        toremove = self.pos[val]    
        last = self.val.pop()
        del self.pos[val]
        if last != val:
            self.val[toremove] = last
            self.pos[last] = toremove
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.val[random.randint(0, len(self.val)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
