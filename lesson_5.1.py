
my_f = open('ls_5.1.txt', 'w', encoding='utf-8')

while True:
    line = input('Введите текст \n')
    if not line:
        break
    my_f.write(line + '\n')
