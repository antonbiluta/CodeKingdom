class Task:
    def __init__(self, name, description, completed=False):
        self.name = name
        self.description = description
        self.completed = completed

    def complete(self):
        # Метод для отметки задания как выполненного
        self.completed = True
        print("Задание \"{}\" выполнено.".format(self.name))

    def __str__(self):
        # Метод для вывода описания задания
        status = "завершено" if self.completed else "не завершено"
        return f"{self.name} ({status}): {self.description}"