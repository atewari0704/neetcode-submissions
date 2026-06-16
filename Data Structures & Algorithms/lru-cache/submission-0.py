class Node:
    def __init__(self,key,val):
        self.key = key # we may not need this because technically the key is gonna come from a dict anyways
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.map = dict()
    

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self,node):
        before,after = self.right.prev,self.right
        node.prev,node.next = before,after
        before.next,after.prev = node,node

    def get(self, key: int) -> int:
        return_val = self.map.get(key,-1)

        #if it exists it moves up
        # remove it and then insert it
        if self.map.get(key):
            self.remove( self.map[key] )
            self.insert( self.map[key] )
            return self.map[key].val
        
        return -1
        

        

    def put(self, key: int, value: int) -> None:

        #if it already exist
        if self.map.get(key):
            self.remove( self.map[key] ) # remove cur version

        # insert new version
        self.map[key] = Node(key,value)
        self.insert( self.map[key] )


        if len(self.map) > self.capacity:
            lru = self.left.next
            
            del self.map[lru.key]
            
            lru.prev.next = lru.next
            lru.next.prev = lru.prev
        
            






        
