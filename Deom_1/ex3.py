# @Time    : 2018/12/8 15:49
# @Email  : wangchengo@126.com
# @File   : ex3.py
# package version:
#               python 3.6
#               sklearn 0.20.0
#               numpy 1.15.2
#               tensorflow 1.5.0

from urllib import parse

url = 'http://www.baidu.com/s?wd=python&username=abc#1'
resutl = parse.urlsplit(url)
print(resutl)
print('scheme:', resutl.scheme)
