duration = ()
print("Для завершения программы введите 0.")
while duration != 0:
    duration = int(input("Введите количество секунд: "))
    sec = str(duration % 60)
    minutes = str(duration % 86400 % 3600 // 60)
    hour = str(duration % 86400 // 3600)
    day = str(duration // 86400)
    if duration < 60:
        print(sec, "сек")
    if 60 <= duration < 3600:
        print(minutes, "мин", sec, "сек")
    if 3600 <= duration < 86400:
        print(hour, "час", minutes, "мин", sec, "сек")
    if 86400 <= duration:
        print(day, "дн", hour, "час", minutes, "мин", sec, "сек")
