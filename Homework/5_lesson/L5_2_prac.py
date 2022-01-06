def odd_nums(stop):
    for el in range(1, stop + 1, 2):
        yield el


def odd_nums_without_yield(stop):
    return (el for el in range(1, stop + 1, 2))


odd_to_15 = odd_nums(15)
print(type(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))


od_to_15_without_yield = odd_nums_without_yield(15)
print(type(od_to_15_without_yield))
print(next(od_to_15_without_yield))
print(next(od_to_15_without_yield))
print(next(od_to_15_without_yield))
print(next(od_to_15_without_yield))
