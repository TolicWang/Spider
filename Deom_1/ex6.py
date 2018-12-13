# @Time    : 2018/12/8 19:54
# @Email  : wangchengo@126.com
# @File   : ex6.py
# package version:
#               python 3.6
#               sklearn 0.20.0
#               numpy 1.15.2
#               tensorflow 1.5.0

from urllib import request
from urllib import parse


def clean_str(string, sep=" "):
    """
    该函数的作用是去掉一个字符串中的所有非中文字符
    :param string: 输入必须是字符串类型
    :param sep: 表示去掉的部分用什么填充，默认为一个空格
    :return: 返回处理后的字符串
    # ，ff0c
    example:
    s = "祝你2018000国庆快乐！"
    print(clean_str(s))# 祝你 国庆快乐
    print(clean_str(s,sep=""))# 祝你国庆快乐
    """

    import re
    string = re.sub(r"[^\u4e00-\u9fff]", sep, string)
    string = re.sub(r"\s{2,}", sep, string)  # 若有空格，则最多只保留2个宽度
    return string.strip()


url = 'https://www.neihan8.com/lxy/index_2.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Referer': 'https://www.neihan8.com/lxy//'
}
req = request.Request(url, headers=headers)
resp = request.urlopen(req)
contents = resp.read().decode('utf-8').split('title=')
all_contents = []
for item in contents:
    temp = clean_str(item)
    if len(temp)<25:
        continue
    all_contents.append(temp)

for i,item in enumerate(all_contents[2:22]):
    print(item,'------->',i)
