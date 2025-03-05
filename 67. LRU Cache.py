class Node:
    """Doubly linked list node"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  # Hashmap to store key -> node mapping
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail  # Connect head to tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove a node from the doubly linked list"""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_end(self, node):
        """Add a node right before the tail (Most Recently Used)"""
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move the node to the most recently used position
            self._add_to_end(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self._remove(self.cache[key])  # Remove existing node
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_end(new_node)

        if len(self.cache) > self.capacity:
            # Remove the least recently used (LRU) node
            lru_node = self.head.next  # First node after dummy head
            self._remove(lru_node)
            del self.cache[lru_node.key]
