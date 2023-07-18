import sys

configFile = open("config.cfg", "r")
lines = configFile.readlines()
config = {}

for line in lines:
    line = line.split("=")
    line = map(str.strip, line)
    key, value = line
    config[key] = value

csv = open(config['data'], 'r')
template = open("static/index.html",  "r")

table = ""
first = csv.readline().split(',')
first[-1] = first[-1][:-1]
first.insert(0, "Nr")

def generateRow(list, firstRow=False):
    ans = ""
    if(firstRow):
        ans += "<tr class=\"first_row\">"
    else:
        ans += "<tr>"
    for coloumn in list:
        ans += "<td>" + coloumn + "</td>"
    return ans

table += generateRow(first, True)
lines = csv.readlines()
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

lines = template.readlines()
output = open("output.html", "w")

for line in lines:
    if("$title$" in line):
        output.write("<h1> REZULTATE " + config['name'] + "</h1>\n")
    elif("$results$" in line):
        output.write(table + "\n")
    else:
        output.write(line)


