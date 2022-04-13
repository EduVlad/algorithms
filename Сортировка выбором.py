a = [3, 2, 6, -1]

def selection_sort(lst):
    res = []
    while len(lst) > 0:
        res.append(min(lst))
        del lst[lst.index(min(lst))]

    return res

print(a)
print(selection_sort(a))
