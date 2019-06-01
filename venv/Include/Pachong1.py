import re

file = open('text.txt','r', encoding='UTF-8')
html = file.read()
file.close()

findall = re.findall("<a href=\"(.*?)\">", html, re.S)


for item in findall:
    sub = re.sub('//', "", item)
    if(item == '#'):
        continue
    print(sub)

