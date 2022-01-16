def parse_logs(path_file="./nginx_logs.txt"):
    with open(path_file, "r", encoding="utf-8") as file:
        for line in file:
            ip = line.split("- -")[0]
            type_and_resource = line.split('"')[1]
            type = type_and_resource.split()[0]
            resource = type_and_resource.split()[1]
            yield ip, type, resource


def find_spammer(path_file="./nginx_logs.txt"):
    with open(path_file, "r", encoding="utf-8") as file:
        counter = {}
        for el in parse_logs():
            counter[el[0]] = counter.get(el[0], 0) + 1
        return max(counter.items(), key=lambda x: x[1])


print(find_spammer())
