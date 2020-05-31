subj = {}
with open('text_6.txt', 'r', encoding='utf-8') as init_f:
    for line in init_f:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        subj[name] = name_sum
print(f'Общее количество часов по предмету - \n {subj}')