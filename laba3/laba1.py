"""
1. Визначте середнє значення всіх елементів послідовності, яка
завершується числом 0. Вводиться послідовність цілих чисел, що
закінчується числом 0 (саме число 0 в послідовність не входить, а
використовується як ознака її закінчення).

Автор: Мовчан Микола
"""

list = []

while True:
    number = int(input("Введіть ціле число (0 тільки для завершення): "))

    if type(number) != int:
        print("Невірний тип даних")
        break
    else:
        if number == 0:
            print(f"Середнє число у списку: {sum(list)/len(list)}")
            break
        else:
            list.append(number)