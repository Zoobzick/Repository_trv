class NoAllNumb(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == "__main__":

    lst = []
    print("Enter 'stop' to quit ")
    while True:
        try:
            inp = input()
            if inp == "stop":
                break
            elif not inp.isdigit():
                raise NoAllNumb()
            else:
                lst.append(int(inp))
        except NoAllNumb:
            print(f"{inp} is not a digit or number")

    print(*lst)