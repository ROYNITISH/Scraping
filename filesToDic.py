import re
import json
file_name="file-S04.txt"
file=open(file_name,"r+")
dicts={}

regex = re.compile('(S\d\d)')
x = regex.search(file_name)
dicts['Season']=x.group(1)


regex = re.compile('(E\d{2})')
for links in file.readlines():
    x = regex.search(links)
    print(x)
    dicts[x.group(1)]=links
dicts_in_json= json.dumps(dicts)
print(dicts_in_json)
file.close()
file=open("file-S04.json","w+")
file.write(dicts_in_json)
