# @Time    : 2018/12/8 15:27
# @Email  : wangchengo@126.com
# @File   : ex1.py
# package version:
#               python 3.6
#               sklearn 0.20.0
#               numpy 1.15.2
#               tensorflow 1.5.0

from urllib import request

resp = request.urlopen('https://www.weibo.com')
print(resp.read(20))  # read(size),readline,readlines,getcode

request.urlretrieve('http://www.baidu.com','baidu.html')# 下载一个网页
request.urlretrieve('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1544264711576&di=e9ff582ae68ee19c697c48d4672e4fcd&imgtype=0&src=http%3A%2F%2Fimg.18183.com%2Fuploads%2Fallimg%2F170612%2F36-1F612155053.jpg','baidu.jpg')# 下载一个网页


