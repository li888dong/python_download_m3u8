# -*-coding:utf-8-*-  
import requests
import os 
import datetime

def download_ts(url):
    download_path = (os.getcwd() + "_" + "download")
    if not os.path.exists(download_path):        
        os.mkdir(download_path)          

    download_path = unicode(download_path, "utf-8")
    #url = 'https://rmfile.dahe.cn/dvkmU5cHhW5RR3MF5avMpnIKpak=/lmQuCL7dJWJAm9yMvojnKawkFceU/0/000000.ts';
    end_index = url.find('.ts');
    start_index = url.rfind('/');

    res = requests.get(url, stream=True)
    filename = url[start_index:end_index]+'.ts';

    with open(download_path+'/'+filename,'ab') as file:
        file.write(res.content)
        file.flush()

def merge_ts():
    download_path = (os.getcwd() + "_" + "download")
    os.chdir(download_path)    
    cmd = "cat * > new.tmp"
    os.system(cmd)
    os.system('rm *.mp4')
    os.rename("new.tmp", "new.mp4")

