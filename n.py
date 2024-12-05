raw_input = input("Введите частоту волны (например, 3x109): ")
formatted_input = raw_input.replace('x', 'e')
print(f"Обработанный ввод: {formatted_input}")

try:
    frequency = float(formatted_input)
    if frequency < 3e9:
        print("Радиоволны")
    elif 3e9 <= frequency < 3e12:
        print("Микроволны")
    elif 3e12 <= frequency < 4e14:
        print("Инфракрасное излучение")
    elif 4e14 <= frequency < 7.5e14:
        print("Видимое излучение")
    elif 7.5e14 <= frequency < 3e17:
        print("Ультрафиолетовое излучение")
    elif 3e17 <= frequency < 3e19:
        print("Рентгеновское излучение")
    elif frequency >= 3e19:
        print("Гамма-излучение")
    else:
        print("Некорректное значение частоты")
except ValueError:
    print("Ошибка: Неправильный формат частоты. Используйте формат, например, '3x109'.")
