class Node:
     def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0 
        self.key_dict = dict()
        self.head = Node(None,None) # dummy Node
        self.tail = self.head # intially the head and tail is the same 
        

    def get(self, key: int) -> int:
        print("get",key)
        if self.key_dict.get(key,None):
            print("triggered", self.key_dict[key])
            self.put(key, self.key_dict[key].value)

            return self.key_dict[key].value
        
        return -1 
        

    def put(self, key: int, value: int) -> None:
        #if the Node already exists
        if self.key_dict.get(key,None):
            curNode = self.key_dict[key]

            curNode.prev.next = curNode.next

            if curNode.next:
                curNode.next.prev = curNode.prev
            else:
                self.tail = curNode.prev # the only time curNode.next won't exist is if it is the tail


            del self.key_dict[key] # we will add it back below
            self.size -= 1
            print("size is now: ",self.size)


        # add to the end
        curNode = Node(key,value)
        self.key_dict[key] = curNode

        self.tail.next = curNode
        curNode.prev = self.tail
        self.tail = curNode
        self.size += 1

        # if we go over
        if self.size > self.capacity:
            print(self.head.next.key if self.head.next else "NOTHING")
            removal = self.head.next
            self.head.next = removal.next
            
            if removal.next:
                removal.next.prev = self.head
            
            del self.key_dict[removal.key]
            self.size -= 1
        
        cur = self.head
        while cur:
            print((cur.key,cur.value))
            cur = cur.next


        return None
        
 