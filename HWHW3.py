with open('text3.txt', 'r') as f:
    workers = []
    salary = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            workers.append(i[0])
        salary.append(i[1])
    print(f'Оклад меньше 20.000 - {workers}, средний оклад - {sum(map(int, salary)) / len(salary)}')
