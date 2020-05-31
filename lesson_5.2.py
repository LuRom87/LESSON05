my_file = open('ls_5.1.txt', 'r', encoding='utf-8')
content = my_file.read()
print(f'Содержимое файла: \n{content}')

my_file = open('ls_5.1.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')

my_file = open('ls_5.1.txt', 'r')
content = my_file.readlines()
for i, value in enumerate(content):
    num = len(value.split())
    print(f'Количество слов {i + 1}-строки {num} слова')


my_file.close()
