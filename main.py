import sys

for arg in sys.argv:
    if("data" in arg):
        path = arg.split("=")[1]
file = open(path, 'r')
template = open("static/index.html",  "r")

table = ""
first = file.readline().split(',')
first[-1] = first[-1][:-1]
first.insert(0, "Nr")

def generateRow(list, className=None):
    ans = ""
    if(className):
        ans += "<tr class=\"" + className + "\">"
    else:
        ans += "<tr>"
    for coloumn in list:
        ans += "<td>" + coloumn + "</td>"
    return ans

table += generateRow(first, "first_row")
lines = file.readlines()
place = 0
for line in lines:
    place += 1
    row = [str(place)] + [x if x != "-1" else "---" for x in line.split(",")]
    row[-1] = row[-1][:-1]
    numberNotSubmitted = 0
    for x in row:
        if(x == "---"):
            numberNotSubmitted += 1
    if(numberNotSubmitted == len(row)-3):
        break
    table += generateRow(row)

print(table)