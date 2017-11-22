import urllib
import requests
import json
import ssl
import zipfile
import os
import sys

ssl._create_default_https_context = ssl._create_unverified_context

def mkdir(filename):
    current_dir=os.getcwd()
    if os.path.exists(os.path.join(current_dir,filename)) == False:
        os.mkdir(os.path.join(os.getcwd(), filename))
    #os.chdir(os.path.join(os.getcwd(), filename))

def parse_url(filename,generate_url):
    final_dir = os.path.join(os.getcwd(), filename)
    url = 'https://apis.meican.com/v2.1/closet/downloadRawLog?client_id=TMorVol3uXnalyM7J9s5MMHZdn8HgoM&client_secret=hQaauYWVcZsJR4zEXMdFY4ogo7lsQOT&pathKey='
    key_url= url + generate_url
    return key_url

def getfile(filename,mode,generate_url):
    final_dir = os.path.join(os.getcwd(), filename)
    key_url=parse_url(filename, generate_url)
    urllib.request.urlretrieve(key_url, os.path.join(final_dir, "logPath.txt"))
    list = open(os.path.join(final_dir, "logPath.txt"))
    line=list.readline()
    list.close()
    os.remove(os.path.join(final_dir, "logPath.txt"))
    #print(line)
    data = json.loads(line)
    #print(data['data']['url'])
    final_url = data['data']['url']
    r = requests.get(final_url)

    if(mode == "a"):
        with open(os.path.join(final_dir,"fileList"), "wb") as code:
            code.write(r.content)
        loglist = open(os.path.join(final_dir, "fileList"))
        line= loglist.readlines()
        for item in line:
            print(line)
    else:
        with open(os.path.join(final_dir, "logDownLoad.zip"), "wb") as code:
            code.write(r.content)
        zipFile = zipfile.ZipFile(os.path.join(final_dir, "logDownLoad.zip"))

        for file in zipFile.namelist():
            zipFile.extract(file, final_dir)
            zipFile.close()

    os.remove(os.path.join(final_dir,"logDownLoad.zip"))
    #os.startfile(r'D:\Program Files\IDM Computer Solutions\UltraEdit\uedit64.exe')
    os.startfile(os.path.join(final_dir, file))

mkdir(sys.argv[1])
getfile(sys.argv[1],sys.argv[2],sys.argv[3])


