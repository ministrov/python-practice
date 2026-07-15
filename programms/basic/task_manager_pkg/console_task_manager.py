""" В этой лекции мы начинаем разработку финального проекта - консольного менеджера задач на Python. Вот основные моменты:

    Создание консольного приложения для управления задачами.
    Возможности: добавление, удаление, изменение задач, получение списка текущих задач, работа с тегами.
    Задачи будут храниться в специальном хранилище, что позволит использовать проект как полноценный таск трекер.
"""
from shlex import split
from task_manager_pkg.commands.help import help_command
from task_manager_pkg.commands.add import add_command
from task_manager_pkg.tasks.tasks import Task
from task_manager_pkg.storage.file import save_task


def main():
    tasks: list[Task] = []
    next_id = 1
    file_path = "task.json"
    print("Task менеджер. help - для справки")

    while True:
        try:
            raw = input("> ").strip()
            parts = split(raw)
            cmd, args = parts[0], parts[1:]

            print(args)

            # print(parts)

            # print(args)

            match cmd.lower():
                case "help":
                    help_command()
                case "add":
                    next_id = add_command(tasks, args, next_id)
                case "list":
                    pass
                case "remove":
                    pass
                case "edit":
                    pass
                case "tags":
                    pass
                case "exit":
                    save_task(file_path, tasks)
                    break
                case _:
                    print("Неизвестная команда")

        except KeyboardInterrupt:
            save_task(file_path, tasks)
            print("\n Завершение приложения...")
            break
        except Exception as e:
            save_task(file_path, tasks)
            print(f"[ERROR]: {e}")


if __name__ == "__main__":
    main()
