import os

current_directory = os.getcwd()

while True:
    command = input(f"{current_directory}> ")

    if command.startswith("pwd"):
        print(current_directory)
    elif command.startswith("cd"):
        _, directory = command.split(" ", 1)
        try:
            os.chdir(directory)
            current_directory = os.getcwd()
        except FileNotFoundError:
            print(f"Папка '{directory}' не существует.")
    elif command.startswith("touch"):
        _, filename = command.split(" ", 1)
        with open(filename, "w") as file:
            pass
    elif command.startswith("cat"):
        _, filename = command.split(" ", 1)
        try:
            with open(filename, "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")
    elif command.startswith("ls"):
        files = os.listdir(current_directory)
        for file in files:
            print(file)
    elif command.startswith("rm"):
        _, filename = command.split(" ", 1)
        try:
            os.remove(filename)
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")
    else:
        print("Неверная команда. Доступные команды: pwd, cd, touch, cat, ls, rm.")

