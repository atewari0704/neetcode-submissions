class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class MyCircularQueue:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.k = k
        self.length = 0
    
    def Node(self,value,next=None):
        self.value = value
        self.next = next

    def enQueue(self, value: int) -> bool:
        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head

            self.head.next = self.tail
            self.tail.next = self.head

            self.length += 1
            return True
        
        elif self.length < self.k:
            self.tail.next = Node(value)
            self.tail = self.tail.next
            self.tail.next = self.head
            self.length += 1
            return True
        
        return False

    def deQueue(self) -> bool:
        if self.length == 0: return False

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return True
        
        else:
            cur = self.head

            for i in range(self.length):
                print(i, cur.value,"->")
                cur = cur.next

            self.head = self.head.next
            self.tail.next = self.head
            self.length -= 1
            return True
        

    def Front(self) -> int:
        return self.head.value if self.head else -1
        

    def Rear(self) -> int:
        return self.tail.value if self.tail else -1
        

    def isEmpty(self) -> bool:
        return self.length == 0
        

    def isFull(self) -> bool:
        return self.length == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()