from random import randint

def counting_sort(items):
    max_elm = max(items)
    dict1 = dict()
    full = []
    for elm in items:
        if elm in dict1:
            dict1[elm].append(elm)
        else:
            dict1[elm] = [elm]
    for i in range(max(items)+1):
        if i in dict1.keys():
            full.extend(dict1[i])
    return full

if __name__ == "__main__":
    items = [randint(1, 100) for i in range(10)]
    print(items)
    print(counting_sort(items))
 