def thesaurus(*args):
    main_list = {}
    for i in sorted(args):
        char = i[0]
        if char not in main_list:
            main_list[char] = list(filter(lambda element: element.startswith(char), args))
    print(main_list)
thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")