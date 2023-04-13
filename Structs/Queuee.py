class Queue:
    __items = list()

    def enqueue(self, new_item):
        self.__items.insert(0, new_item)

    def dequeue(self):
        return self.__items.pop()

    def __str__(self) -> str:
        return self.__items.__str__()

if __name__ == "__main__":
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q)
    print(q.dequeue())
    print(q)