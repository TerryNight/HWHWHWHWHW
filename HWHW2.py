f = open("text2.txt", "w")
my_str = "I\nlove\nprogramming\nvery\nmuch"
f.writelines(my_str)
k = 1
for el in my_str:
    s = 0
    if el == "\n":
       k = k + 1
       s += len(el)
       print(f"words = {s}")
print(f"Колличество строк в файле {k}")
