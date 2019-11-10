a = {}
b = 0
with open("text6.txt", "r") as f:
    for el in f:
        lab, lec, sem = el.split()
        a[b] = int(lab) + int(lec) + int(sem)
    print(f"Колличество часов по предмету: {a}")