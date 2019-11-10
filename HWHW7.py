import json
name = {}
form = {}
prof = {}
iz = {}
with open("text7.txt", "w") as f:
    f.write("f1 " + "OOO " + "1000" + " " + "5000" + "\n" + "f2 " + "PAO " + "7000" + " " + "300000 " + "\n" +
            "f3 " + "OOO " + "30000" + " " + "1500")
    for line in f:
        name, form, prof, iz = line.split()
