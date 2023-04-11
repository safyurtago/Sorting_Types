from random import randint

def insertion_sort():
    lst = [randint(1,50) for i in range(10)]
    print(lst)
    step = 0
    for i in range(1, len(lst)):
        j = i - 1
        pivot = lst[i]
        while j >= 0 and lst[j] > pivot:
            step += 1
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = pivot
    print("step:", step)
    return lst

print(insertion_sort())
