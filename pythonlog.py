import urllib
import requests
import json
import ssl
import zipfile
import os
import sys

ssl._create_default_https_context = ssl._create_unverified_context

count=0
count_wanted=0
def mkdir(filename):
    current_dir=os.getcwd()
    if os.path.exists(os.path.join(current_dir,filename)) == False:
        os.mkdir(os.path.join(os.getcwd(), filename))
    #os.chdir(os.path.join(os.getcwd(), filename))

def parse_url(filename,mode):
    global count
    global count_wanted
    final_dir = os.path.join(os.getcwd(), filename)

    list_url = 'https://apis.meican.com/v2.1/closet/rawLogList?client_id=TMorVol3uXnalyM7J9s5MMHZdn8HgoM&client_secret=hQaauYWVcZsJR4zEXMdFY4ogo7lsQOT'
    urllib.request.urlretrieve(list_url, os.path.join(final_dir, "loglist.txt"))
    list_all = open(os.path.join(final_dir, "loglist.txt"))
    line=list_all.readline()
    data = json.loads(line)
    list_all.close()
    os.remove(os.path.join(final_dir, "loglist.txt"))
    for item in data['data']['list']:
        if filename in item:
            #print(item)
            count = count +1
            #print(count)
    for item in data['data']['list']:
        if filename in item:
            count_wanted = count_wanted +1
            if count_wanted == count - int(mode):
                #generate_url = item
                print(item)
                break

    url = 'https://apis.meican.com/v2.1/closet/downloadRawLog?client_id=TMorVol3uXnalyM7J9s5MMHZdn8HgoM&client_secret=hQaauYWVcZsJR4zEXMdFY4ogo7lsQOT&pathKey='
    key_url= url + item
    return key_url


def getfile(filename,mode):
    final_dir = os.path.join(os.getcwd(), filename)
    key_url=parse_url(filename,mode)
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

    if(int(mode) == 99):
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
getfile(sys.argv[1],sys.argv[2])


