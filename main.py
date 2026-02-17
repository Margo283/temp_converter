# temp_converter.py
"""
Конвертер температури Цельсій ↔ Фаренгейт з підтримкою кількох перетворень.
"""

import argparse


def c_to_f(c: float) -> float:
    return (c * 9 / 5) + 32


def f_to_c(f: float) -> float:
    return (f - 32) * 5 / 9


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Конвертер температури C ↔ F")
    parser.add_argument("value", type=float, nargs="?", help="Температура (якщо не вказано — інтерактивний режим)")
    parser.add_argument("-m", "--mode", choices=["c2f", "f2c"], default="c2f",
                        help="Напрямок: c2f (Цельсій → Фаренгейт), f2c (Фаренгейт → Цельсій)")
    args = parser.parse_args()

    print("Конвертер температури (Цельсій ↔ Фаренгейт)\n")

    if args.value is not None:
        # Одноразове перетворення через аргументи
        if args.mode == "c2f":
            result = c_to_f(args.value)
            print(f"{args.value:.1f} °C → {result:.1f} °F")
        else:
            result = f_to_c(args.value)
            print(f"{args.value:.1f} °F → {result:.1f} °C")
    else:
        # Інтерактивний режим
        while True:
            choice = input("1 = C → F, 2 = F → C, q = вихід: ").strip().lower()
            if choice in ('q', 'quit', 'exit'):
                break
            if choice not in ('1', '2'):
                print("Виберіть 1 або 2")
                continue

            try:
                temp = float(input("Температура: "))
                if choice == '1':
                    print(f"{temp:.1f} °C → {c_to_f(temp):.1f} °F")
                else:
                    print(f"{temp:.1f} °F → {f_to_c(temp):.1f} °C")
            except ValueError:
                print("Введіть число")
