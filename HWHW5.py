with open('text5.txt', 'x') as f:
    line = input('Введите цифры через пробел \n')
    f.writelines(line)
    my_numbs = line.split()
    print(sum(map(int, my_numbs)))




