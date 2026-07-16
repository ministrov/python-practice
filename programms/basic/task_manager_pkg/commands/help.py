""" Модуль вывода помощи пользователю """


def help_command():
    print(""" Команды: 
        add <title> [prio=low|med|high] [due=YYYY-MM-DD] [tags=a,b,c] - Добавить
            (title из нескольких слов оборачивай в кавычки: add "Купить молоко" prio=high)
        list [by=prio|due] - Показать список отфильтрованный по приоритеты либо дате
        done <id> - Выполнить
        edit <id> - [title=...] [prio=...] [due=YYYY-MM-DD]
        remove <id> - Удалить
        tags <id> add|remove <tag> - Изменить теги
        help - Помощь
        exit - Выход
        
""")
