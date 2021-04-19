class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {} # key: node->prev
        self.head = LinkedNode()
        self.tail = self.head
        
    def pushback(self, node):
        # put node to back of the queue
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = self.tail.next
        
    def popfront(self):
        # pop front node
        del self.hash[self.head.next.key]
        if self.head.next:
            self.head.next = self.head.next.next
            self.hash[self.head.next.key] = self.head
        
    def kick(self, prev):
        # move a node to back of the queue
        curt = prev.next
        if curt == self.tail:
            return
        prev.next = curt.next
        if curt.next != None:
            self.hash[curt.next.key] = prev
            curt.next = None
        self.pushback(curt)
        

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        ret = self.hash[key].next.value
        self.kick(self.hash[key])
        return ret

    def put(self, key: int, value: int) -> None:
        if key not in self.hash:
            self.pushback(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.popfront()
        else:
            self.hash[key].next.value = value
            self.kick(self.hash[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
