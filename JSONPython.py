import urllib.request,urllib.parse,urllib.error
import json

sum = 0
c = 0
data = input("Enter Location:")
print("Retrieving",data)
fhand = urllib.request.urlopen(data)
d = fhand.read().decode()

print("Retrieved",len(d),"characters")

info = json.loads(d)
di = info["comments"]

for item in di:
    sum = sum + int(item['count'])
    c = c + 1

print("Count:", c)
print("Sum:", sum)