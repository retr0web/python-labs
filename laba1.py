"""
1. Враховуючи ціле число n - кількість хвилин, що пройшли з опівночі, - скільки годин і 
хвилин відображаються на екрані 24-годинного цифрового годинника? Програма повинна
друкувати два числа: кількість годин (від 0 до 23) і кількість хвилин (від 0 до 59). 
Наприклад, якщо n = 150, то після опівночі пройшло 150 хвилин, тобто зараз 2:30 ранку. 
Так що програма повинна друкувати 2 30.
"""
print("Завдання 1")

n = int(input("Введіть кількість хвилин після опівночі: "))

hours = n // 60
minutes = n % 60

print(f"{hours} {minutes}")
print("------------------------------------------------------")

"""
2.  Вводиться додатне дійсне число a. Виведіть його першу цифру після десяткового дробу.
При розв’язуванні цього завдання не можна користуватися умовною конструкцією і циклом.
"""
print("Завдання 2")

a = float(input("Введіть додатне дійсне число a: "))
print(f"Перша цифра після десяткового дробу: {int((a * 10) % 10)}")

print("------------------------------------------------------")

"""
3.  Напишіть програму для друку літери З висотою 5 рядків за допомогою введеного
користувачем символу.
"""
print("Завдання 3")

symbol = input("Введіть символ для літери З: ")

print(" " + symbol + symbol + symbol + " ")
print(symbol + " " + " " + " " + symbol)
print(" " + " " + symbol + symbol + " ")
print(symbol + " " + " " + " " + symbol)
print(" " + symbol + symbol + symbol + " ")

print("------------------------------------------------------")

"""
4.  Напишіть програму для друку літери З висотою 5 рядків за допомогою введеного
користувачем символу.
"""
print("Завдання 4")

number = input("Введіть додатне ціле трицифрове число: ")
print(f"Сума цифр числа: {int(number[0]) + int(number[1]) + int(number[2])}")

print("------------------Кінець програми---------------------")