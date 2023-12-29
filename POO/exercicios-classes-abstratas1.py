from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self) -> float:
        pass


class Developer(Employee):
    def calculate_bonus(self) -> None:
        bonus = 0.2 * self.salary
        print(f"Developer {self.name}:\nSalário: {self.salary:.2f}\n"
              f"Bonificação: {bonus:.2f}")


class Analyst(Employee):
    def calculate_bonus(self):
        bonus = 0.3 * self.salary
        print(f"Analyst {self.name}:\nSalário: {self.salary:.2f}\n"
              f"Bonificação: {bonus:.2f}")


class Manager(Employee):
    def calculate_bonus(self):
        bonus = 0.4 * self.salary
        print(f"Manager {self.name}:\nSalário: {self.salary:.2f}\n"
              f"Bonificação: {bonus:.2f}")


def main():
    jose = Developer("José", 2000)
    maria = Analyst("Maria", 3000)
    maria_jose = Manager("Maria José", 4000)

    jose.calculate_bonus()
    maria.calculate_bonus()
    maria_jose.calculate_bonus()


if __name__ == "__main__":
    main()
