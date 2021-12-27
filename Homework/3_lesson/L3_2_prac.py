def num_translate_adv(number):
    numbers = {'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'teen': 'десять'}
    if number[0].islower():
        print(numbers.get(number))
    else:
        print(numbers.get(number.lower()).capitalize())


num_translate_adv("five")
