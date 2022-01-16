def merger():
    # проверка длины списков (если длина списка имён больше длины списка хобби, выходим с завершающим кодом 1)
    with open("users.csv", "r", encoding="utf-8") as f1, \
            open("hobby.csv", "r", encoding="utf-8") as f2:

        if len(f1.readlines()) < len(f2.readlines()):
            return "Process finished with exit code 1"

    with open("users.csv", "r", encoding="utf-8") as f1, \
            open("hobby.csv", "r", encoding="utf-8") as f2, \
            open("users_hobby.txt", "w", encoding="utf-8") as out:
        for sent in f1:
            hobby = f2.readline().strip()
            out.write(f"{sent.strip()}: {hobby if hobby else None}\n")


merger()
