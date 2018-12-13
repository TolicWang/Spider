# @Time    : 2018/12/8 15:40
# @Email  : wangchengo@126.com
# @File   : ex2.py
# package version:
#               python 3.6
#               sklearn 0.20.0
#               numpy 1.15.2
#               tensorflow 1.5.0

from urllib import parse
from urllib import request

params = {'name': '张三', 'age': 18}
result = parse.urlencode(params)
print(result)


#------------------编码----------------------

# url = 'http://www.baidu.com/s?wd=刘德华' 会报错
url = 'http://www.baidu.com/s'
params = {'wd': '刘德华'}
qs = parse.urlencode(params)
url += ('?'+qs)
resp = request.urlopen(url)
# print(resp.read())

#------------------解码----------------------
params = {'name': '张三', 'age': 18}
result = parse.urlencode(params)
print(result)
result = parse.parse_qs(result)
print(result)
