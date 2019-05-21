import urllib.request

weburl = urllib.request.urlopen("https://gmail.com")

content = weburl.read()
print(content)
