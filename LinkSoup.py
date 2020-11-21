import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input("Enter URL: ")
c = int(input("Enter count: "))
pos = int(input("Enter position: "))
print("Retrieving:", url)
i = 1
while i<=c :
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')

    #Retrieve all the span tags
    tags = soup('a')
    t = tags[pos-1].get('href',None)
    print("Retrieving:", t)
    i = i + 1
    url = t




