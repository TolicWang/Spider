# @Time    : 2018/12/8 16:36
# @Email  : wangchengo@126.com
# @File   : ex5.py
# package version:
#               python 3.6
#               sklearn 0.20.0
#               numpy 1.15.2
#               tensorflow 1.5.0

from urllib import request
from urllib import parse
import json
import pandas as pd
import time

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E7%AE%97%E6%B3%95?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=sug&suginput=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E7%AE%97'
}

all_info = []
for pages in range(1, 31, 1):
    data = {
        'first': 'false',
        'pn': pages,
        'kd': '深度学习a'
    }
    req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
    resp = request.urlopen(req)
    contents = resp.read().decode('utf-8')
    print(contents)
    print('-----------------------------------------------page:', pages)
    try:
        data = json.loads(contents)
        results = data['content']['positionResult']['result']
        for company in results:
            all_info.append([company['companyFullName'], company['city'], company['industryField'],
                             company['positionName'], company['salary'], company['workYear'], company['education'],
                             company['companySize']])
    except:
        names = ['公司名称', '位置', '行业', '职位', '薪资', '工作经验', '学历', '公司规模']
        data = pd.DataFrame(all_info, columns=names)
        data.to_excel('./result.xlsx', index=False, encoding='utf-8')
    time.sleep(10)
names = ['公司名称', '位置', '行业', '职位', '薪资', '工作经验', '学历', '公司规模']
data = pd.DataFrame(all_info, columns=names)
data.to_excel('./deeplearninga.xlsx', index=False, encoding='utf-8')
