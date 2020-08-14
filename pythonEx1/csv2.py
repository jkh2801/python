'''
Created on 2020. 8. 14.

@author: GDJ24
'''
import codecs
filename = "cctv.csv"
csv = codecs.open(filename, "r", "UTF8").read() # String 형으로 한번에 읽어낸다.
data = []
rows = csv.split("\r\n")
for row in rows :
    if row == "" : continue
    cells = row.split(",")
    data.append(cells)
outfp = open("cctv.txt", "w", encoding="UTF8")
for c in data :
    print(c[0], c[1], c[2], c[3])
    outfp.write(" ".join(map(str,c)) + "\n")