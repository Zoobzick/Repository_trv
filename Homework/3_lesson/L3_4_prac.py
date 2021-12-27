def thesaurus_adv(*full_names):
    dic = {}
    for full_name in sorted(full_names):
        name, sec_name = full_name.split()
        if dic.get(sec_name[0]) is None:
            dic[sec_name[0]] = {name[0]: [full_name]}
        elif dic[sec_name[0]].get(name[0]) is None:
            dic[sec_name[0]][name[0]] = [full_name]
        else:
            dic[sec_name[0]][name[0]].append(full_name)
    for key, value in sorted(dic.items()):
        print(f' "{key}": \n\t {value}')


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Анна Савельева")
