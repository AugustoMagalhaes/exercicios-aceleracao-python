def sum_list(numbers: list[int]) -> int:
    """Exercício 1"""
    return sum(numbers)


def filter_by_first_letter(values: str, letter: str) -> list[str]:
    """Exercício 2"""
    return [
        v for v in values if v.startswith(letter)
    ]


class Book():
    """Exercício 3"""
    def __init__(self, book: str, author: str, pages: int) -> None:
        self.book = book
        self.author = author
        self.pages = pages

    def __str__(self) -> None:
        return (f"Livro: {self.book} é do autor {self.author} "
                f"e tem {self.pages} páginas")


class Car():
    """Exercício 4"""
    def __init__(self, model: str, year: int) -> None:
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self) -> None:
        if self.speed + 10 <= 200:
            self.speed += 10
            print(f"Vruum accelerating... speed: {self.speed}")
        else:
            print(f"Car is already at max speed: {self.speed}")

    def deaccelerate(self) -> None:
        if self.speed - 10 >= 0:
            self.speed -= 10
            print(f"Shhhhhhh deaccelerating... speed now: {self.speed}")
        else:
            print("Car is turned off")

    def get_speed(self) -> int:
        return self.speed

    def __str__(self) -> str:
        return f"Car {self.model} made in {self.year} is at {self.speed} km/h"


numbers = [1, 2, 3, 4, 5]
print(sum_list(numbers))

animals = ["cachorro", "gato", "elefante", "girafa"]
CHAR = "g"

print(filter_by_first_letter(animals, CHAR))

car = Car("Gol 2.0", 1999)

car.accelerate()
car.deaccelerate()
car.deaccelerate()
car.accelerate()
print(car)
