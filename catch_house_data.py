import requests
from bs4 import BeautifulSoup
import re
import time
'''
pip install bs4 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --proxy 87.254.212.121:8080
'''
proxy = {
    'http':'87.254.212.121:8080',
    'https':'87.254.212.121:8080'
}
heads = {}
heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

response = requests.get("http://www.tmsf.com/housing/", headers=heads,proxies=proxy)
house_data = re.findall("全市 <font class=\"f24 f_blue\">(\d+) </font> 套挂牌真房源",response.text)[0]
line = time.strftime('%Y-%m-%d',time.localtime(time.time()))+":"+house_data+"\n"
with open("house_data.txt","a+") as fh:
    fh.write(line)

