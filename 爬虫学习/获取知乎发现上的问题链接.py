#!/usr/bin/python3
# @Author: WLP
# @name: 获取知乎发现上的问题链接.py
# @date 2020-05-07 14:56

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import requests

def main():
    headers = {'user-agent' : 'Baiduspider'}
    proxies = {'http': 'http://122.114.31.177:808'}
    base_url = 'https://zhihu.com/'
    seed_url = urljoin(base_url, 'explore')
    resp = requests.get(url=seed_url, headers = headers, proxies = proxies)
    soup = BeautifulSoup(resp.text, 'lxml')
    # print(soup.find_all('a',{'href': re.compile(r'^//www.zhihu.com')}))
    href_regex = re.compile(r'^/question')
    link_set = set()
    for a_tag in soup.find_all('a', {'href': href_regex}):
        print(a_tag.text)
        if 'href' in a_tag.attrs:
            href = a_tag.attrs['href']
            full_url = urljoin(base_url, href)
            link_set.add(full_url)
    print('Total %d question pages found' % len(link_set))
    print(link_set)

if __name__ == '__main__':
    main()