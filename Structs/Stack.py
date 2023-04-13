class Stack:
    __items = []

    def push(self, new_item):
        self.__items.append(new_item)
    
    def pop(self):
        return self.__items.pop()

    def __str__(self) -> str:
        return self.__items.__str__()


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s)

    print(s.pop())
    print(s.pop())
    print(s)

    s.pop()