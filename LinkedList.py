class LinkedListItem:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class LinkedList:
    first = None

    def push(self, item):
        # print(self.first)
        if self.first is None:
            self.first = LinkedListItem(item)
        else:
            cur = self.first
            while cur.next is not None:
                cur = cur.next

            cur.next = LinkedListItem(item)
    
    # def __str__(self) -> str:
    #     return 

if __name__ == "__main__":
    l = LinkedList()

    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    print(l)