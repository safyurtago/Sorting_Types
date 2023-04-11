from random import randint

def merge(left, right):
    full = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            full.append(left.pop(0))
        else:
            full.append(right.pop(0))
    if len(left) > 0:
        full.extend(left)
    if len(right) > 0:
        full.extend(right)
    return full
    
def merge_sort(items):
    if len(items) < 2:
        return items    
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    print("LEFT: ", left, "RIGHT: ", right)
    return merge(left, right)

if __name__ == "__main__":
    items = [randint(1, 100) for i in range(10)]
    print(items)
    print(merge_sort(items))