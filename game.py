import random

FIELD_SIZE = 7
EMPTY = "."
SHIP = "S"
HIT = "X"
MISS = "O"

# Показать игровое поле
def display(field):
    print("\n".join(" ".join(row) for row in field))

# Размещение кораблей (просто случайно)
def place_ships(field):
    for _ in range(10):  # 10 кораблей
        while True:
            x, y = random.randint(0, FIELD_SIZE - 1), random.randint(0, FIELD_SIZE - 1)
            if field[x][y] == EMPTY:
                field[x][y] = SHIP
                break

# Основной игровой цикл
def main():
    field = [[EMPTY] * FIELD_SIZE for _ in range(FIELD_SIZE)]
    place_ships(field)
    attempts = 0

    while any(SHIP in row for row in field):  # Пока есть непотопленные корабли
        display(field)
        try:
            x, y = map(int, input("Enter your shot (row column): ").split())
            if 1 <= x <= FIELD_SIZE and 1 <= y <= FIELD_SIZE:  # Проверка на допустимый ввод
                if field[x - 1][y - 1] == SHIP:
                    field[x - 1][y - 1] = HIT
                    print("Hit!")
                elif field[x - 1][y - 1] == EMPTY:
                    field[x - 1][y - 1] = MISS
                    print("Miss!")
                else:
                    print("Already shot here!")
                attempts += 1
            else:
                print("Coordinates out of range!")
        except ValueError:
            print("Invalid input! Enter two numbers.")

    print(f"You won in {attempts} shots!")

if __name__ == "__main__":
    main()
