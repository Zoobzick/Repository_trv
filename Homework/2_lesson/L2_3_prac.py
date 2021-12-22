mylist = ["в", "5", "часов", "17", "минут", "температура", "воздуха", "была", "+5", "градусов"]
i = 0
el = 0
while i < len(mylist):
    if mylist[i].isdigit() or (mylist[i][1:].isdigit()):
        if len(mylist[i]) == 2 and mylist[i][0] not in "+-":
            mylist[i] = '"' + str(mylist[i]) + '"'
        elif len(mylist[i]) < 2:
            mylist[i] = '"' + "0" + str(mylist[i]) + '"'
        elif mylist[i][0] in "+-" and len(mylist[i][1:]) < 2:
            mylist[i] = '"' + mylist[i][0] + str("0") + str(mylist[i][1:]) + '"'
        elif mylist[i][0] in "+-" and len(mylist[i][1:]) == 2:
            mylist[i] = '"' + mylist[i][0:3] + '"'
    i += 1
while el < len(mylist):
    if mylist[el]:
        mylist.insert(el + 1, " ")
        el += 1
    el += 1
print("".join(mylist))
