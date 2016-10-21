import sqlite3

ls = []
with open('GB.txt', 'r') as f:
    for line in f:
        ls.append(line.split('\t'))

data = []
for i in ls:
    d = []
    d.append(i[3])
    d.append(i[0])
    d.append(i[2])
    d.append(i[1])
    data.append(d)

conn = sqlite3.connect('GB.db')
c = conn.cursor()

c.execute("CREATE TABLE gb (country text, region text, city text, postcode text)")

for i in data_list:
    c.execute("INSERT INTO gb VALUES (?,?,?,?)", i)
conn.commit()

c.close()
conn.close()
