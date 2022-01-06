import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []


def my_filter(*arg):
    return (arg[i] for i in range(1, len(arg)) if arg[i] > arg[i - 1])



print(list(my_filter(*src)))
print(type(my_filter(*src)))
print(sys.getsizeof(my_filter(*src)))