class MyZeroDiv(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == "__main__":
    from sys import exit

    a = 0
    b = 0
    try:
        a = float(input("Input a: "))
        b = float(input("Input b: "))
    except:
        print("Incorrect input")
        exit(1)

    try:
        if b == 0:
            raise MyZeroDiv("Can't div by 0")
        print(f"Result {a}/{b} = {a/b}")
    except MyZeroDiv as ex:
        print(ex)
