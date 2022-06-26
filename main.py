import re
import zipfile

EXPRESSION = ".+ - - \[(([0-2][0-9])|(3[0-1]))/[A-Z][a-z]{2}/[0-9]{4}:((01:59)|(0[2-9]:[0-5][0-9])|(1[0-5]:[0-5][0-9])|(16:[0-1][0-9])|(16:2[0-7])):[0-5][0-9]( -[0-9]+)*\] \"GET .+\.((png)|(jpeg)|(jpg)|(gif)) HTTP/1\.0\" 200 .+"
EXPRESSION2 = "/[^/]+\.((gif)|(jpg)|(jpeg)|(png))"

mp = {"gif": set(), "jpg": set(), "png": set(), "jpeg": set()}
with zipfile.ZipFile("access_log_Jul95.zip", 'r') as zip_ref:
    zip_ref.extractall()

with open("access_log_Jul95.zip", "r", encoding='windows-1252', errors='ignore') as f:
    for s in f:
        if re.match(EXPRESSION, s):
            n = re.search("/[^/]+\.(gif)", s)
            if n:
                mp["gif"].add(n.group())
            n = re.search("/[^/]+\.(jpg)", s)
            if n:
                mp["jpg"].add(n.group())
            n = re.search("/[^/]+\.(jpeg)", s)
            if n:
                mp["jpeg"].add(n.group())
            n = re.search("/[^/]+\.(png)", s)
            if n:
                mp["png"].add(n.group())
print(f"gif: {len(mp['gif'])}")
print(f"png: {len(mp['png'])}")
print(f"jpg: {len(mp['jpg'])}")
print(f"jpeg: {len(mp['jpeg'])}")