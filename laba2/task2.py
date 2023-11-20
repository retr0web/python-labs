"""
2. Напишіть програму, у якій користувач вводить значення поточної
дати: день, місяць і рік (цілі числа), а програма виводить вчорашню
дату у форматі: дд.мм.рррр.

Автор: Мовчан Микола
"""
from datetime import datetime, timedelta

enter_date = input("Enter today's date separated by dots (18.11.2023): ")

year = int(enter_date.split(".")[2])
month = int(enter_date.split(".")[1])
day = int(enter_date.split(".")[0])

current_date = datetime(year, month, day)

yesterday = current_date - timedelta(days=1)

date_format = "%d.%m.%Y"

print(f"Вчора було {yesterday.strftime(date_format)}")




