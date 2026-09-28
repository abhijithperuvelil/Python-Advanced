import csv
# f=open("data.csv","r")
# content=csv.reader(f)
# for row in content:
#     print(row)
# f.close()
import csv
f = open("book.csv", "w", newline="")
content = [
    ['title', 'author', 'place'],
    ['book 1', 'john', 'ekm'],
    ['book 2', 'sam', 'tvm']
]
writer = csv.writer(f)
writer.writerows(content)
f.close()