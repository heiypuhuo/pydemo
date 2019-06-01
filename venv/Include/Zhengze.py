import re
code = "dfadxxIxxfasdfadfaxxlovexx4we5r123sdfaxxyouxxasdf"
res = re.findall("xx(.*?)xx",code)
print(res)