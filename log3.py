import urllib.request
import re
import os
import ssl
print ('downloading')
raw_url = 'https://apis.meican.com/v2.1/closet/rawLogList?client_id=TMorVol3uXnalyM7J9s5MMHZdn8HgoM&client_secret=hQaauYWVcZsJR4zEXMdFY4ogo7lsQOT&pathKey=rawlog/closet-383/version-1100473/2017-11-17_20-22/log2017_11_17_20_22.zip'
ssl._create_default_https_context = ssl._create_unverified_context
r = urllib.request.urlopen(raw_url)
with open("download.zip", "wb") as code:
     code.write(r.content)