import json
import subprocess
import time

from bs4 import BeautifulSoup
## from selenium import webbrowser
from util import my_decode, __create__table, InsertData
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 1.获取相应网站搜索地址
# 2.获取某个招聘页面的详细信息
# 3.提取重要信息
# 4.保存到mysql

# 1 在前程无忧搜索大数据

for i in range(1, 17):
    time.sleep(1)
    url = '''curl 'https://search.51job.com/list/190000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,{0}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=' \
      -H 'Connection: keep-alive' \
      -H 'sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"' \
      -H 'Accept: application/json, text/javascript, */*; q=0.01' \
      -H 'X-Requested-With: XMLHttpRequest' \
      -H 'sec-ch-ua-mobile: ?0' \
      -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36' \
      -H 'Sec-Fetch-Site: same-origin' \
      -H 'Sec-Fetch-Mode: cors' \
      -H 'Sec-Fetch-Dest: empty' \
      -H 'Referer: https://search.51job.com/list/190000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=' \
      -H 'Accept-Language: zh-CN,zh;q=0.9' \
      -H 'Cookie: guid=16aebebc19341bb94b9d924683c289cf; slife=lowbrowser%3Dnot%26%7C%26; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60190000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60190000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B4%F3%CA%FD%BE%DD%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21collapse_expansion%7E%601%7C%21; adv=adsnew%3D0%26%7C%26adsnum%3D2004282%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttps%253A%252F%252Fwww.baidu.com%252Fother.php%253Fsc.a00000j0RcO3woxzZZeDjkqLcotl7ATKBDZuRsulOuGVXxh3uso1a5HXh6p1hz6pzT3fmEk7IVTg-yqsDrNih7YGOiR8yXlLK4BG4ZYsRDJLvg4WdxVHRFrYYKy4GwifbCYLJ1-_qinZ-tYFlSeGFSq8o15-O_XBfDKZExyCCDTIOsCrKrht2z1wlDvKmVhbHHbpPIe6v71bY8kFwAbybXvQHNTa.DR_NR2Ar5Od66CHnsGtVdXNdlc2D1n2xx81IZ76Y_uQQr1F_zIyT8P9MqOOgujSOODlxdlPqKMWSxKSgqjlSzOFqtZOmzUlZlS5S8QqxZtVAOtIOtHOuS81wODSgL35SKsSXKMqOOgfESyOHjGLY51xVOeNH5exS88Zqq1ZgVm9udSnQr1__oodvgvnehUrPL72xZgjX1IIYJN9h9merzEuY60.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqkea11neXYtT0IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqkea11neXYtT0ThPv5HD0IgF_gv-b5HDdnWc1rjb3njf0UgNxpyfqnHn3PjfdP1D0UNqGujYknjT4nWcdnsKVIZK_gv-b5HDkPHnY0ZKvgv-b5H00pywW5R9rf6KWThnqPjbLrHR%2526ck%253D1450.2.93.292.150.184.179.198%2526dt%253D1613619772%2526wd%253D%2525E5%252589%25258D%2525E7%2525A8%25258B%2525E6%252597%2525A0%2525E5%2525BF%2525A7%2526tpl%253Dtpl_11534_23295_19442%2526l%253D1522389804%2526us%253DlinkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E3%25252580%25252590%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A751Job%252525E3%25252580%25252591-%25252520%252525E5%252525A5%252525BD%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%252525E5%252525B0%252525BD%252525E5%2525259C%252525A8%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A7%2521%252526linkType%25253D%26%7C%26' \
      --compressed'''
    cmd = url.format(str(i))
    print(cmd)
    # 发起请求
    process = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = ''
    # 处理响应
    # 解码
    if process.returncode == 0:
        print("请求成功")
        result = my_decode(process.stdout)
    else:
        print("请求失败")
        result = my_decode(process.stderr)
    print(result)
    # 字符串转字典
    jsonob = json.loads(result)
    # 处理第一条信息
    ddd = jsonob["engine_search_result"][0]
    print(ddd)
    jobid = ddd["jobid"]
    print(jobid)
    # 获取详情地址
    job_href = ddd["job_href"]
    print(job_href)



    # 这里设置表名
    table_name = "qcwy_bigdata"
    # 这里设置需要的字典数据

    # __create__table(table_name, ddd)
    for j in jsonob["engine_search_result"]:
        InsertData(table_name, j)
    print('插入%d页完成' %i)