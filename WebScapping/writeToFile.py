import requests

res = requests.get('https://www.dn.se/')
res.raise_for_status()
playFile = open('dn.html', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
