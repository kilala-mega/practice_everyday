class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.positions = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.array.append(val)
        self.positions[val].add(len(self.array)-1)
        return len(self.positions[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.positions:
            return False
        last_val = self.array.pop()
        self.positions[last_val].remove(len(self.array))
        if len(self.positions[last_val]) == 0:
            del self.positions[last_val]
        if val != last_val:
            toremove_pos = self.positions[val].pop()
            if len(self.positions[val]) == 0:
                del self.positions[val]
            self.positions[last_val].add(toremove_pos)
            self.array[toremove_pos] = last_val
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.array[random.randint(0, len(self.array)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
