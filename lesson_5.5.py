def summa():
    try:
        with open('text_5.txt', 'w+') as my_file:
            line = input('Введите цифры через пробел \n')
            my_file.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summa()