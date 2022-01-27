class Road:
    _lenght = float
    _width = float

    def __init__(self, width, lenght):
        self._width = width
        self._lenght = lenght

    def materials(self, expense: float, thickness: float):
        return self._lenght * self._width * expense * thickness


r = Road(40, 30)
print(r.materials(25, 10))
