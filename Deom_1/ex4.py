# @Time    : 2018/12/8 15:58
# @Email  : wangchengo@126.com
# @File   : ex4.py
# package version:
#               python 3.6
#               sklearn 0.20.0
#               numpy 1.15.2
#               tensorflow 1.5.0

from urllib import request

url = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
# resp = request.urlopen(url)
# print(resp.read())

#-------------------------自定义请求头-------------------

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
res = request.Request(url,headers=headers)
resp = request.urlopen(res)
print(resp.read())