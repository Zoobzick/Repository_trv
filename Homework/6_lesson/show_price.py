PRICE_FILE = "./bakery.csv"


if __name__ == "__main__":

    import sys

    with open(PRICE_FILE, "r+", encoding="utf-8") as price_list:
        param = len(sys.argv)
        if param == 1:
            print(price_list.read())
        if param == 2:
            for line in price_list.readlines()[int(sys.argv[1]) - 1:]:
                print(line)
        elif param == 3:
            i = 0
            for line in price_list:
                i += 1
                if i >= int(sys.argv[1]):
                    if i > int(sys.argv[2]):
                        break
                    print(line, end="")


