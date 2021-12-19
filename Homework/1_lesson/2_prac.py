values_cube = [i**3 for i in range(1, 1000, 2)]
result = 0
for i in values_cube:
    summ = 0
    digit = i
    while digit != 0:
        m = digit % 10
        digit = digit / 10
        summ = int(summ + m)
        if digit == 0 and summ % 7 == 0:
            result += i
print("result_first = " + str(result))
sec_result = 0
for i in values_cube:
    i += 17
    summ = 0
    digit = i
    while digit != 0:
        m = digit % 10
        digit = digit / 10
        summ = int(summ + m)
        if digit == 0 and summ % 7 == 0:
            sec_result += i
print("result_second = " + str(sec_result))
