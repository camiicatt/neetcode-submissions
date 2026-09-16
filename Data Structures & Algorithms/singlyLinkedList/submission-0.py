class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        #Dummy Node
        self.head = ListNode(-1)
        self.tail = self.head 

    def get(self, index: int) -> int:
        current = self.head.next
        i = 0

        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next 
        return -1 #out of bounds 

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        #edge case for tail pointer

        if not new_node.next:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        current = self.head

        while i < index and current:
            #move current to node before the taret node
            i += 1 
            current = current.next

        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next 
            return True
        return False

        #what if deleted tail, need to update tail pointer
        

    def getValues(self) -> List[int]:
        current = self.head.next
        res =[]
        while current:
            res.append(current.val)
            current = current.next 
        return res

