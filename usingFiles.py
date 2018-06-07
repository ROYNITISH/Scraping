from scrapperObj import scrapper
file=open("file-Black%20Mirror.txt",'r+')
for m in file.readlines():
    obj=scrapper(m)
    obj.operation()