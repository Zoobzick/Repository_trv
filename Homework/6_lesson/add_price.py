PRICE_FILE = "./bakery.csv"


if __name__ == "__main__":

    import sys
    input_price = sys.argv[1]

    with open(PRICE_FILE, "a", encoding="utf-8") as price_list:
        price_list.write(input_price + "\n")
