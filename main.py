import csv


with open('file.csv', newline='') as file:
    reader = csv.reader(file, delimiter=";")
    first = []
    c =[]
    for st in reader:
        first.append(float(st[0].split(",")[2]))
        for i in range(2,12):
            c.append(float(st[i].split(",")[2]))

    res_all = []   
    for i in range(10):
        res =[]
        for t in range(100):
            res.append(c[i])
            i += 10
        res_all.append(res)

res_final = []

for i in first:
    for j in res_all:
        for t in j:
            if i - t > 0:
                res_final.append(f"Больше {i} - {t}")
            else:
                res_final.append(f"Меньше  {i} - {t}")
