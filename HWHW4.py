rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_f = []
with open("text4.txt", "r") as f:
    for el in f:
        el = el.split(' ', 1)
        new_f.append(rus_dict[el[0]] + '  ' + el[1])
print(new_f)

with open('file_4_new.txt', 'w') as f_2:
    f_2.writelines(new_f)