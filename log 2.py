# coding = UTF-8
# 爬取李东风PDF文档,网址：https://apis.meican.com/v2.1/closet/rawLogList?client_id=TMorVol3uXnalyM7J9s5MMHZdn8HgoM&client_secret=hQaauYWVcZsJR4zEXMdFY4ogo7lsQOT

import urllib.request
import re
import os
import ssl

# open the url and read
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    page.close()
    return html

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?.+?\.pdf)'
    url_re = re.compile(reg)
    url_lst = url_re.findall(html.decode('gb2312'))
    return(url_lst)

def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    f = open(file_name, 'r')

    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)


#root_url = 'http://www.math.pku.edu.cn/teachers/lidf/docs/textrick/'

#root_url = 'https://apis.meican.com/v2.1/closet/rawLogList?client_id=TMorVol3uXnalyM7J9s5MMHZdn8HgoM&client_secret=hQaauYWVcZsJR4zEXMdFY4ogo7lsQOT'
raw_url = 'https://apis.meican.com/v2.1/closet/rawLogList?client_id=TMorVol3uXnalyM7J9s5MMHZdn8HgoM&client_secret=hQaauYWVcZsJR4zEXMdFY4ogo7lsQOT&pathKey=rawlog/closet-383/version-1100473/2017-11-17_20-22/log2017_11_17_20_22.zip'

ssl._create_default_https_context = ssl._create_unverified_context
#print (urllib.request.urlopen("root_url").read())

html = getHtml(raw_url)
#url_lst = getUrl(html)

os.mkdir('zip_download')
os.chdir(os.path.join(os.getcwd(), 'zip_download'))

getFile(raw_url)


#for url in url_lst[:]:
#    url = root_url + url
