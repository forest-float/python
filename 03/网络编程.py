# -*- coding: utf-8 -*-
# @Author: wlp
# @Date:   2020-04-22 16:56:15
# @Last Modified by:   forest-float
# @Last Modified time: 2020-04-22 17:16:12

import requests
from threading import Thread
from time import time 
class download_thread(Thread):
	def __init__(self,url):
		super().__init__()
		self._url = url
	@property
	def url(self):
		return self._url
	
	def run(self):
		filename = self._url[self._url.rfind('/') + 1:]
		resp = requests.get(self._url)
		with open("aaa.jpg",'wb') as f:
			f.write(resp.content)



url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1587556970565&di=7733f80a5e33510a3f5337b85388d259&imgtype=0&src=http%3A%2F%2Fp1.meituan.net%2Fdeal%2Fc92b6b67b83d4fc294224028699f92df109612.jpg"
down = download_thread(url)
down.start()
down.join()



