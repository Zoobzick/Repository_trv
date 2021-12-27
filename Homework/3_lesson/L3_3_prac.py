def thesaurus(*names):
    dic = {}
    for name in sorted(names):
        if dic.get(name[0]):
            dic[name[0]].append(name)
        else:
            dic[name[0]] = [name]
    for key, value in dic.items():
        print(f' "{key}": {value}')


thesaurus("Иван", "Мария", "Петр", "Илья")
