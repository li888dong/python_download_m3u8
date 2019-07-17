# -*-coding:utf-8-*-  
# 李栋 2018-9-27
import requests
import downloadts


def get_url(domain, url):
    # 读取m3u8文件
    links = requests.get(url)
    links = links.text.splitlines()

    # 将地址放进列表
    links_list = []
    for eachline in links:
        if not eachline.startswith('#'):
            links_list.append(eachline.replace('\n', ''))

    # 读取视频地址并且放入列表

    for link in links_list:
        print(domain + link)
        if link.endswith('.ts'):
            # 下载ts文件
            downloadts.download_ts(domain + link)
    
            

    # 合并ts文件
    downloadts.merge_ts()


get_url('https://rmfile.dahe.cn', 'https://rmfile.dahe.cn/video/mp4/20190717/1563326102496446.m3u8')
