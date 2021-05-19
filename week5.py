import urllib.request as ur
import xml.etree.ElementTree as ET


url = input("Enter location: ")
#http://py4e-data.dr-chuck.net/comments_42.xml
print('Retrieving: ', url)

uh = ur.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
results = tree.findall('.//count')

total = 0
for item in results:
    total = total + int(item.text)

print('Count: ', len(results))
print('Sum: ', total)
