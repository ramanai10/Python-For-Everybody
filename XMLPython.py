import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
import requests

c = 0
s = 0
count = 0

data = input("Enter Location:")
print("Retrieving",data)
fhand = urllib.request.urlopen(data)

for line in fhand:
    c = c + len(line)

print("Retrieved",c,"characters")

tree = ET.fromstring(requests.get(data).text)

#Find the sum of all numbers within <count> tag
for item in tree.findall('.//count'):
    s = s + int(item.text)
    count = count + 1

print("Count:",count)
print("Sum:",s)    