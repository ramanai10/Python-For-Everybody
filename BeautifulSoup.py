import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input("Enter- ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
s = 0
c = 0

#Retrieve all the span tags
tags = soup('span')
for tag in tags:
    s += int(tag.contents[0])
    c = c + 1

print("Count",c)
print("Sum",s)    

