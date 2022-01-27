class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income["wage"] * self._income["bonus"]


worker = Position("Vlad", "Troshev", "GRR", 5, 7)

print(worker.get_full_name())
print(worker.get_total_income())

