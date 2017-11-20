import urllib
import requests
import json
import ssl
import zipfile
import os

ssl._create_default_https_context = ssl._create_unverified_context

current_pwd=os.getcwd()
url = 'https://apis.meican.com/v2.1/closet/downloadRawLog?client_id=TMorVol3uXnalyM7J9s5MMHZdn8HgoM&client_secret=hQaauYWVcZsJR4zEXMdFY4ogo7lsQOT&pathKey=rawlog/closet-383/version-1100473/2017-11-17_20-22/log2017_11_17_20_22.zip'
print( "downloading...........")
urllib.request.urlretrieve(url, os.path.join(os.getcwd(),"logPath.txt"))
f = open(os.path.join(os.getcwd(),"logPath.txt"))
line=f.readline()
os.remove(os.path.join(os.getcwd(),"logPath.txt"))
print(line)
data=json.loads(line)
print(data['data']['url'])
parse_url=data['data']['url']

r = requests.get(parse_url)
with open("logDownLoad.zip", "wb") as code:
     code.write(r.content)

zipFile = zipfile.ZipFile(os.path.join(os.getcwd(),"logDownLoad.zip"))

for file in zipFile.namelist():
  zipFile.extract(file, os.getcwd())
  zipFile.close()

  os.remove(os.path.join(os.getcwd(),"logDownLoad.zip"))

os.system('/Applications/SublimeText.app')

