mylist = [7.05, 5.81, 69, 15.4, 192.8, 94.35, 8.5, 48.41, 6.95, 39.6, 121, 108.05]
i = 0
while i < len(mylist):
    if mylist[i] % 1 == 0:
        mylist[i] = str(mylist[i]) + " руб." + " 00 коп."
    elif mylist[i] % 1 * 100 >= 10:
        rub = round(mylist[i] // 1)
        kop = round(((mylist[i] % 1) * 100))
        mylist[i] = str(rub) + " руб. " + str(kop) + " коп."
    else:
        rub = round(mylist[i] // 1)
        kop = "0" + str(round(((mylist[i] % 1) * 100)))
        mylist[i] = str(rub) + " руб. " + str(kop) + " коп."
    i += 1
print(mylist)
