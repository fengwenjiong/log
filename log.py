import urllib2
print "downloading with urllib2"
url = "https://apis.meican.com/v2.1/closet/rawLogList?client_id=TMorVol3uXnalyM7J9s5MMHZdn8HgoM&client_secret=hQaauYWVcZsJR4zEXMdFY4ogo7lsQOT/log2017_10_31_18_00_22_18_01.zip"
f = urllib2.urlopen(url) 
data = f.read() 
with open("demo2.zip", "wb") as code:     
    code.write(data)
