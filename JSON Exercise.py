import urllib.request, urllib.error, urllib.parse
import json
import ssl

#input the URL
site=input("Enter the URL:")
#set to ignore SSL Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#create the needed lists
fh = urllib.request.urlopen(site, context=ctx).read()
json_fh=json.loads(fh)
comments=json_fh['comments']


#create your for loop
total=0
for comment in comments:
    total+=comment['count']
print(total)

