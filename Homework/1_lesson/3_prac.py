exception = [11, 12, 13, 14]
for i in range(1, 101):
    if i in exception:
        print(str(i) + " процентов")
    elif i % 10 == 1:
        print(str(i) + " процент")
    elif 1 < i % 10 < 5:
        print(str(i) + " процента")
    else:
        print(str(i) + " процентов")
