def users():
    mydic = {}
    with open("users.csv", "r", encoding="utf-8") as f1, \
            open("hobby.csv", "r", encoding="utf-8") as f2:

        if len(f1.readlines()) < len(f2.readlines()):
            return "Process finished with exit code 1"

    with open("users.csv", "r", encoding="utf-8") as f1, \
            open("hobby.csv", "r", encoding="utf-8") as f2:
        for sent in f1:
            name = sent.strip()
            hobby = f2.readline().strip()
            if not hobby:
                hobby = None
            mydic[name] = hobby

    with open("users_result.txt", "w", encoding="utf-8") as users_result:
        for key, value in mydic.items():
            users_result.writelines(f"{key}: {value}\n")
        return mydic


print(users())
