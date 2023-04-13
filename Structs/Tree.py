from random import randint

class Tree:
    def __init__(self, item) -> None:
        self.item = item
        self.right = None
        self.left = None

    def insert(self, new_item):
        if self.item > new_item:
            if self.left is None:
                self.left = Tree(new_item)
            else:
                self.left.insert(new_item)
        else:
            if self.right is None:
                self.right = Tree(new_item)
            else:
                self.right.insert(new_item)

    def __str__(self) -> str:
        left = right = ""
        if self.left is not None:
            left += f"{self.left}"
        if self.right is not None:
            right += f"{self.right}"
        return f"{left} {self.item} {right}"

if __name__ == "__main__":
    lst = [randint(1, 100) for i in range(10)]
    print(lst)
    t = Tree(lst[0])
    for i in lst[1:]:
        t.insert(i)
    print(t)