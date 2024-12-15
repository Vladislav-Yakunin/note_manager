from datetime import datetime

# Создаем словарь для хранения данных о заметке
note = {}
# Записываем данные от пользователя

note["username"] = input("Введите имя пользователя: ")

# Запрашиваем несколько заголовков и добавляем их в список
note["titles"] = []
for n in range(3):
    title = input(f"Введите заголовок заметки {n + 1}: ")
    note["titles"].append((title))

note["content"] = input("Введите описание заметки: ")

note["status"] = input("Введите статус заметки: ")

temp_created_data = input('Введите дату создания заметки в формате "дд-мм-гггг": ')
temp_issue_data = input('Введите дату истечения заметки в формате "дд-мм-гггг": ')
# Преобразование строки в обьекты даты и вывод даты без года
note["created_data"] = datetime.strptime(temp_created_data, "%d-%m-%Y").strftime("%d-%m")
note["issue_data"] = datetime.strptime(temp_issue_data, "%d-%m-%Y").strftime("%d-%m")

print("\nСобранные данные по заметке: ")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")