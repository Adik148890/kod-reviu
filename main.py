# Список дел — простая программа для ведения списка задач

tasks = []


def show_help():
    """Показывает список доступных команд."""
    print("Доступные команды:")
    print("  add   - добавить задачу")
    print("  list  - показать все задачи")
    print("  help  - показать эту подсказку")
    print("  exit  - выйти из программы")


def add_task():
    """Спрашивает у пользователя текст задачи и добавляет её в список."""
    text = input("Введите задачу: ")
    if text == "":
        print("Задача не может быть пустой!")
        return
    tasks.append(text)
    print("Задача добавлена.")


def show_tasks():
    """Выводит все задачи с номерами."""
    if len(tasks) == 0:
        print("Список дел пуст.")
        return
    number = 1
    for task in tasks:
        print(f"{number}. {task}")
        number += 1


print("Привет! Это программа «Список дел».")
show_help()

# Главный цикл: ждём команду и выполняем её
while True:
    command = input("> ")
    if command == "add":
        add_task()
    elif command == "list":
        show_tasks()
    elif command == "help":
        show_help()
    elif command == "exit":
        print("Пока!")
        break
    else:
        print("Неизвестная команда. Введите help, чтобы увидеть список команд.")