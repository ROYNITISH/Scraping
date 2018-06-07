from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import re
#txt = open('pel.txt','w+')
try:
    url="http://dl6.downloadoo.ir/TV.Show/"
    html = urlopen(url)
except HTTPError as e:
    print("error code:"+str(e.getcode())+",cannot open url")
    exit(0)

    soup=bs(html,'html.parser')
    str=soup.title.get_text()
    regTitle = re.compile(r'[^Index of/][\w+.]+')
    searchR = re.findall(regTitle,str)




#txt.write(soup.head.title.get_text()+'\n')


