import urllib.request as ur
import xml.etree.ElementTree as et 

url=input("Enter URL:")
html=ur.urlopen(url).read() 

tree=et.fromstring(html)
counts = tree.findall('.//count')

total=0
for counts in counts:
    total=total+int(counts.text)
    
print(total)
