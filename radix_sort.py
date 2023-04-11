# from random import randint

# def radix_sort(items, a):
#     length = len(items) - 1
#     if a > 100:
#         return items
#     dict1 = dict()
#     for i in items:
#         if i%a in dict1: 
#             dict1[i%a].append(i)
#         else:
#             dict1[i%a] = [i]
#     items.clear()
#     for i in range(length):
#         if i in dict1.keys():
#             items.extend(dict1[i])
#     dict1.clear()
#     return radix_sort(items, a*10)


# if __name__ == "__main__":
#     items = [randint(1, 100) for i in range(10)]
#     print(items)
#     print(radix_sort(items, 10))