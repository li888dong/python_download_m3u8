# -*-coding:utf-8-*-  

import requests
import json
import downloadts 

def get_url(domain,url):

	# 读取m3u8文件
	links = requests.get(url);
	links = links.text.splitlines();

	# 将地址放进列表
	links_list = [];
	for eachline in links:
		if not eachline.startswith('#'):
			links_list.append(eachline.replace('\n',''))


	# 读取视频地址并且放入列表

	for link in links_list:
		res = requests.get(domain+link);
		for url in res.text.splitlines():
			if url.endswith('.ts'):
				downloadts.download_ts(domain+url)

	# 合并ts文件
	downloadts.merge_ts()

get_url('https://rmfile.dahe.cn','https://rmfile.dahe.cn/12a5d8f3-215c-450a-8f5c-275fb3a348ab.m3u8')

