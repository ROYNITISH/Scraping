from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import re
class scrapper:
    #just a base constructor
    def __init__(self,url):
        if url!='':
            self.url=url
    #checking blank url
        else:
            print("blank")
    #function creates a txt with parameter
    def createFile(self,name):
        file=open("file-"+name+".txt","w+")
        return file
    #operations of scrapping
    def operation(self):
        #regex to the extract file name
        #to improve
        regex = re.compile("/([\w \d\-\.%]*)/$")
        #str = "http://dl6.downloadoo.ir/TV.Show/Z/ Zen/"
        x = regex.search(self.url)
        f=self.createFile(x.group(1))

        try:
            html = urlopen(self.url)
        except HTTPError as e:
            print("error code:" + str(e.getcode()) + ",cannot open url")
            exit(0)
        #extracting the htmlParseTree
        soup=bs(html,"lxml")
        #f.write(soup.title.get_text()+".txt"+"\n")
        #if a url has newline at the last element it creates problem in this code.
        if(self.url[-1]=='\n'):
            self.url=self.url[0:-1]

        for link in soup.find_all('a'):
            if not(link.__contains__('../')):
                if link.__contains__('http://'):
                    #print(link.get('href'))
                    f.writelines(link.get('href'))
                    f.write("\n")
                else:
                    f.write(self.url)
                    f.write((link.get('href')))
                    #urlChild = self.url + str(link.get('href'))
                    print(self.url,(link.get('href')))
                    #f.write(urlChild)
                    f.write("\n")

        f.close()

