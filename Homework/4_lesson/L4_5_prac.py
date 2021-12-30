from utils import currency_rates, splitter
import sys


if __name__ == "__main__":
        currency_name = sys.argv[1:]
        if len(currency_name) < 1:
            print("Don't forget to enter your currency name")
        else:
            currency_name = currency_name.pop(0)
            print(currency_rates(currency_name))