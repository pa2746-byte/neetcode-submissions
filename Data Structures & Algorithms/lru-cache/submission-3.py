class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #key, Node

        self.left = ListNode(0,0)
        self.right = ListNode(0,0)

        self.left.next = self.right
        self.right.prev = self.left        

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

    def remove(self,node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        #update positions
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        #update positions
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=ListNode(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
