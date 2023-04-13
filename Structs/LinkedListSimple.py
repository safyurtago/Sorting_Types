class LinkedList:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

    def push(self, new_item):
        cur = self
        while cur.next is not None:
            cur = cur.next
        
        cur.next = LinkedList(new_item)
    
    def pop(self):
        cur = prev = self
        while cur.next is not None:
            prev = cur
            cur = cur.next
        prev.next = None
        return cur.item

    def size(self):
        count = 1
        cur = self
        while cur.next is not None:
            count += 1
            cur = cur.next
        return count

    def __str__(self) -> str:
        return f"{self.item} {self.next}"

if __name__ == "__main__":
    lst = LinkedList(0)
    lst.push(1)
    lst.push(2)
    lst.push(3)
    lst.push(4)
    print(lst)
    print(lst.pop())
    print(lst.pop())
    print(lst)