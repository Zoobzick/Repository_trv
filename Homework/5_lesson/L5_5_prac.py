from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def my_filter(*arg):
    filtered = set()
    for el in arg:
        if el not in filtered:
            filtered.add(el)
        else:
            filtered.discard(el)
    return (i for i in arg if i in filtered)

start = perf_counter()

print(list(my_filter(*src)))

print(perf_counter() - start)

print(type(my_filter(*src)))
