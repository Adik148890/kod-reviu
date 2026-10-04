# Список дел — простая программа для ведения списка задач
import os

tasks = []
l2 = []


def show_help():
    """Показывает список доступных команд."""
    print("Доступные команды:")
    print("  add   - добавить задачу")
    print("  list  - показать все задачи")
    print("  done  - отметить задачу выполненной")
    print("  del   - удалить задачу")
    print("  save  - сохранить задачи в файл")
    print("  help  - показать эту подсказку")
    print("  exit  - выйти из программы")


def add_task():
    """Спрашивает у пользователя текст задачи и добавляет её в список."""
    text = input("Введите задачу: ")
    if text == "":
        print("Задача не может быть пустой!")
        return
    tasks.append(text)
    l2.append(False)
    print("Задача добавлена.")


def show_tasks():
    """Выводит все задачи с номерами."""
    if len(tasks) == 0:
        print("Список дел пуст.")
        return
    number = 1
    for task in tasks:
        if l2[number - 1] == True:
            print(f"{number}. [x] {task}")
        else:
            print(f"{number}. [ ] {task}")
        number += 1


def done():
    number = 1
    for task in tasks:
        if l2[number - 1] == True:
            print(f"{number}. [x] {task}")
        else:
            print(f"{number}. [ ] {task}")
        number += 1
    n = int(input("Номер задачи: "))
    l2[n - 1] = True
    print("Готово!")


def d():
    number = 1
    for task in tasks:
        if l2[number - 1] == True:
            print(f"{number}. [x] {task}")
        else:
            print(f"{number}. [ ] {task}")
        number += 1
    n = int(input("Номер задачи: "))
    print("тут", n)
    # tasks.remove(n)
    tasks.pop(n)
    print("Удалено!")


def stats():
    c = 0
    for x in l2:
        if x == True:
            c = c + 1
    p = c / len(tasks) * 100
    print("Выполнено", c, "из", len(tasks))
    print("Это", p, "%")


def save():
    f = open("tasks.txt", "w")
    for t in tasks:
        f.write(t)
    f.close()
    print("Сохранено!")


print("Привет! Это программа «Список дел».")
show_help()

# Главный цикл: ждём команду и выполняем её
while True:
    command = input("> ")
    if command == "add":
        add_task()
    elif command == "list":
        show_tasks()
    elif command == "done":
        done()
    elif command == "del":
        d()
    elif command == "stats":
        stats()
    elif command == "save":
        save()
    elif command == "help":
        show_help()
    elif command == "exit":
        print("Пока!")
        break
    else:
        print("Неизвестная команда. Введите help, чтобы увидеть список команд.")