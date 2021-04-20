import collections
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None
        
class DoubleLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None) # dummy Node
        self._sentinel.prev = self._sentinel
        self._sentinel.next = self._sentinel
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self.size += 1
    
    def pop(self, node=None):
        if self.size == 0:
            return
        if node is None:
            node = self._sentinel.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        node.prev = None
        node.next = None
        return node
    
class LFUCache:

    def __init__(self, capacity: int):
        self.nodes = dict()
        self.freqs = collections.defaultdict(DoubleLinkedList)
        self.capacity = capacity
        self.minfreq = 0
        self.size = 0
        
    def update(self, node):
        freq = node.freq
        self.freqs[freq].pop(node)
        if self.minfreq == freq and not self.freqs[freq]:
            self.minfreq += 1
        node.freq += 1
        freq +=1
        self.freqs[freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        self.update(self.nodes[key])
        return self.nodes[key].value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.nodes:
            self.update(self.nodes[key])
            self.nodes[key].value = value
        else:
            if self.size == self.capacity:
                node = self.freqs[self.minfreq].pop()
                del self.nodes[node.key]
                self.size -= 1
            newnode = Node(key, value)
            self.nodes[key] = newnode
            self.freqs[1].append(newnode)
            self.minfreq = 1
            self.size += 1
