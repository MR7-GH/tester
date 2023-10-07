import urllib.request,re,pathlib,ssl
from bs4 import BeautifulSoup

targetUrl = ""
if targetUrl == "" :
    print("Please Enter your url (use http:// | https://) : ")
    targetUrl = input()
    
req = urllib.request.Request(targetUrl, headers={ 'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' })
gcontext = ssl.SSLContext()  # Only for gangstars
contents = str(urllib.request.urlopen(req, context=gcontext).read())
# print(contents)


# parsing html
# it can find urls with a tags
soup = BeautifulSoup(contents, 'html.parser') 
# traverse paragraphs from soup
for data in soup.find_all("span"):
    txt = data.get_text()
    m = re.search(".*(\.ir|\.com|\.co|\.io|\.net|\.online|\.shop).*",txt)
    if m != None or m != "" :
        print(str(txt))
    
    