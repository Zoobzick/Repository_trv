import sys


def merger(users_path, hobby_path, out_path):
    # проверка длины списков (если длина списка имён больше длины списка хобби, выходим с завершающим кодом 1)
    with open(users_path, "r", encoding="utf-8") as f1, \
            open(hobby_path, "r", encoding="utf-8") as f2:

        if len(f1.readlines()) < len(f2.readlines()):
            return "Process finished with exit code 1"

    with open(users_path, "r", encoding="utf-8") as f1, \
            open(hobby_path, "r", encoding="utf-8") as f2, \
            open(out_path, "w", encoding="utf-8") as out:
        for sent in f1:
            hobby = f2.readline().strip()
            out.write(f"{sent.strip()}: {hobby if hobby else None}\n")


if __name__ == "__main__":
    users_name = ""
    hobby_name = ""
    out_name = ""

    if len(sys.argv[1:]) >= 3:
        users_name = sys.argv[1]
        hobby_name = sys.argv[2]
        out_name = sys.argv[3]
        exit(merger(users_path=users_name, hobby_path=hobby_name, out_path=out_name))
