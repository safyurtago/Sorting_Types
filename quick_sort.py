from random import randint

def qucik_sort(items):
    
    if len(items) < 2:
        return items
    low, mid, high = [], [], []
    middle = items[len(items)//2]

    for i in items:

        if i < middle:
            low.append(i)
        elif i > middle:
            high.append(i)
        else:
            mid.append(i)
        
    return qucik_sort(low) + mid + qucik_sort(high)

if __name__ == "__main__":
    items = [randint(1, 100) for i in range(10)]
    print(items)
    print(qucik_sort(items))
 