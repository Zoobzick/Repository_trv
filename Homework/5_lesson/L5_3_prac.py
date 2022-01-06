import sys
from time import perf_counter

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена',
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def my_gen():
    return ((tutors[i], None) if i > len(klasses) - 1 else (tutors[i], klasses[i])  # 1
            for i in range(0, len(tutors)))
    # return ((tut, None) if klass > len(klasses) - 1 else (klasses[klass], tut)
    #         for klass, tut in enumerate(tutors))


start = perf_counter()

for el in my_gen():
    print(el)

print(perf_counter() - start)

print(sys.getsizeof(my_gen()))

print(type(my_gen()))
