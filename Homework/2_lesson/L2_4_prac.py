prof_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
i = 0
for el in prof_name:
    split_name = prof_name[i].split(" ")
    name = split_name.pop().lower().capitalize()
    i += 1
    print("Привет, " + name + "!")
