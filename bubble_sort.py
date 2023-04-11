from random import randint

lst = [randint(1, 40) for i in range(10)]

def bubble_sort(lst):
    step = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            step += 1
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    print("step:", step)
    return lst


print(bubble_sort(lst))