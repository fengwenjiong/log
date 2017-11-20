import requests
print ("downloading with requests")
url = 'https://apis.meican.com/v2.1/closet/rawLogList?client_id=TMorVol3uXnalyM7J9s5MMHZdn8HgoM&client_secret=hQaauYWVcZsJR4zEXMdFY4ogo7lsQOT&pathKey=rawlog/closet-383/version-1100473/2017-11-17_20-22/log2017_11_17_20_22.zip'
r = requests.get(url)
with open("pythontest.zip", "wb") as code:
     code.write(r.content)