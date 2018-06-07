import re
regex=re.compile('/([\w \d-]*)/$')
str="http://dl6.downloadoo.ir/TV.Show/1-9/"
x=regex.search(str)
print((x.group(1)))

