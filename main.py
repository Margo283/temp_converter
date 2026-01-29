def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("Конвертер температури (C ↔ F)")
print("-" * 35)

while True:
    choice = input("\n1 = C → F, 2 = F → C, q = вихід: ")
    if choice.lower() == 'q':
        break
    
    try:
        temp = float(input("Введіть температуру: "))
        if choice == '1':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C → {result:.1f}°F")
        elif choice == '2':
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F → {result:.1f}°C")
        else:
            print("Невірний вибір")
    except ValueError:
        print("Введіть число!")
