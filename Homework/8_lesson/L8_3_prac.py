def type_logger(callback):
    def wrapper(*args):
        result = callback(*args)
        for i in args:
            print(f'{i}: {type(i)}')
        return result

    return wrapper


@type_logger
def calc_box_cube(x):
    return x ** 3


@type_logger
def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if not text.endswith("."):
        text += "."
    return text


print(calc_box_cube(3))

print(correct_sentence("о дивный новый мир"))
