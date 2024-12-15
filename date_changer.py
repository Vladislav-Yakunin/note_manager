from datetime import datetime

username = "Владислав"

title = "Сходить в магазин"

content = ("\nмолоко\nяйца\nтворог")

status = "все взял"

# создаем переменные
temp_created_data = "10-11-2024"
temp_issue_data = "11-11-2024"
# Преобразование строки в обьекты даты и вывод даты без года
created_data = datetime.strptime(temp_created_data, "%d-%m-%Y").strftime("%d-%m")
issue_data = datetime.strptime(temp_issue_data, "%d-%m-%Y").strftime("%d-%m")

print("Вы ввели следующие данные")
print("Имя пользователя: ", username)
print("Заголовок заметки: ", title)
print("Описание заметки: ", content)
print("Статус заметки: ", status)
print("Дата создания заметки: ", created_data)
print("Дата истечения заметки: ", issue_data)