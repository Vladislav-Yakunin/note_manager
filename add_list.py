from datetime import datetime
# Создание переменных
username = input("Введите имя пользователя: ")

# Запрашиваем несколько заголовков и добавляем их в список
titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append((title))

content = input("Введите описание заметки: ")

status = input("Введите статус заметки: ")

temp_created_data = input('Введите дату создания заметки в формате "дд-мм-гггг": ')
temp_issue_data = input('Введите дату истечения заметки в формате "дд-мм-гггг": ')
# Преобразование строки в обьекты даты и вывод даты без года
created_data = datetime.strptime(temp_created_data, "%d-%m-%Y").strftime("%d-%m")
issue_data = datetime.strptime(temp_issue_data, "%d-%m-%Y").strftime("%d-%m")

print("Вы ввели следующие данные:")
print("Имя пользователя: ",username)
print("Заголовки заметки: ",titles)
print("Описание заметки: ",content)
print("Статус заметки: ",status)
print("Дата создания заметки: ",created_data)
print("Дата истечения заметки: ",issue_data)