import os
import datetime
from babel.dates import format_date

configFile = open("config.cfg", "r")
lines = configFile.readlines()
config = {}

for line in lines:
    line = line.split("=")
    line = map(str.strip, line)
    key, value = line
    if key == 'task_ids':
        value = value.split(",")
        value = [x.strip() for x in value]
    config[key] = value

csv = open(config['data'], 'r')
template = open("static/index.html",  "r")

table = ""
first = csv.readline().split(',')
first[-1] = first[-1][:-1]
first.insert(0, "Nr")

def generateRow(list, firstRow=False):
    ans = ""
    if firstRow:
        ans += "<tr class=\"first_row\">"
    else:
        ans += "<tr>"
    for idx, coloumn in enumerate(list):
        if 2 <= idx and idx < len(list)-1 and firstRow == True:
            if len(config['task_ids']) > 0:
                ans += "<td><a href=\"https://kilonova.ro/problems/" + config['task_ids'][idx-2] + "\">" + coloumn + "</a></td>"
            else:
                ans += "<td><a href=\"" + config["task_ids"][idx-2] + "</a>" + coloumn + "</td>"
        else:
            ans += "<td>" + coloumn + "</td>"
    return ans

table += generateRow(first, True)
lines = csv.readlines()
place = 0
rows = []
for line in lines:
    place += 1
    row = [str(place)] + [x if x != "-1" else "---" for x in line.split(",")]
    row[-1] = row[-1][:-1]
    numberNotSubmitted = 0
    for x in row:
        if x == "---":
            numberNotSubmitted += 1
    if numberNotSubmitted == len(row)-3:
        break
    if len(rows) > 0:
        if(row[-1] == rows[-1][-1]):
            row[0] = rows[-1][0]
    rows.append(row)
    table += generateRow(row)

lines = template.readlines()
output = open("static/output.html", "w")

for line in lines:
    if "$title$" in line:
        output.write("<h1> REZULTATE " + config['name'] + "</h1>\n")
    elif "$results$" in line:
        output.write(table + "\n")
    elif "$images$" in line:
        output.write("<img src=\"../" + config['left_logo'] + "\" class=\"l_logo\">\n")
        output.write("<img src=\"../" + config['right_logo'] + "\" class=\"l_logo\">\n")
    elif "$clock$" in line:
        d = datetime.datetime.now()
        time = format_date(d, format="long", locale='ro')
        output.write("<p class=\"clock\">" + time + "</p>\n")
    else:
        output.write(line)
output.close()

os.chdir("static")
command = "wkhtmltopdf --enable-local-file-access -O landscape output.html output.pdf"
os.system(command)
os.remove("output.html")
os.rename("output.pdf", "../output.pdf")