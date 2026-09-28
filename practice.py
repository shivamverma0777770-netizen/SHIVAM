import csv
with open("student.csv","w+",newline='') as f:
    writer=csv.writer(f)
    l=[['Name','marks1','marks2'],['Shivam',14,56],['Verma',56,45]]
    writer.writerows(l)

with open("student.csv","r") as f:
    rows=csv.DictReader(f)
    for row in rows:
        print(row)

with open("student.csv","r") as f:
    rows=csv.reader(f)
    for row in rows:
        print(row)
