# 1.从数据查询jobid和job_href
# 2.根据job_href访问地址
# 3.拿到详情
# 4.将jobid和job_href和详情存到detail表中
import subprocess
import time

from bs4  import BeautifulSoup

from util import select_table, my_decode, get_content_between_tables, __insert__

url2 = """curl '{}' \
  -H 'Connection: keep-alive' \
  -H 'Cache-Control: max-age=0' \
  -H 'sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Sec-Fetch-Site: none' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Cookie: guid=16aebebc19341bb94b9d924683c289cf; slife=lowbrowser%3Dnot%26%7C%26; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60190000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60190000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B4%F3%CA%FD%BE%DD%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21collapse_expansion%7E%601%7C%21; adv=adsnew%3D0%26%7C%26adsnum%3D2004282%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttps%253A%252F%252Fwww.baidu.com%252Fother.php%253Fsc.a00000j0RcO3woxzZZeDjkqLcotl7ATKBDZuRsulOuGVXxh3uso1a5HXh6p1hz6pzT3fmEk7IVTg-yqsDrNih7YGOiR8yXlLK4BG4ZYsRDJLvg4WdxVHRFrYYKy4GwifbCYLJ1-_qinZ-tYFlSeGFSq8o15-O_XBfDKZExyCCDTIOsCrKrht2z1wlDvKmVhbHHbpPIe6v71bY8kFwAbybXvQHNTa.DR_NR2Ar5Od66CHnsGtVdXNdlc2D1n2xx81IZ76Y_uQQr1F_zIyT8P9MqOOgujSOODlxdlPqKMWSxKSgqjlSzOFqtZOmzUlZlS5S8QqxZtVAOtIOtHOuS81wODSgL35SKsSXKMqOOgfESyOHjGLY51xVOeNH5exS88Zqq1ZgVm9udSnQr1__oodvgvnehUrPL72xZgjX1IIYJN9h9merzEuY60.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqkea11neXYtT0IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqkea11neXYtT0ThPv5HD0IgF_gv-b5HDdnWc1rjb3njf0UgNxpyfqnHn3PjfdP1D0UNqGujYknjT4nWcdnsKVIZK_gv-b5HDkPHnY0ZKvgv-b5H00pywW5R9rf6KWThnqPjbLrHR%2526ck%253D1450.2.93.292.150.184.179.198%2526dt%253D1613619772%2526wd%253D%2525E5%252589%25258D%2525E7%2525A8%25258B%2525E6%252597%2525A0%2525E5%2525BF%2525A7%2526tpl%253Dtpl_11534_23295_19442%2526l%253D1522389804%2526us%253DlinkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E3%25252580%25252590%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A751Job%252525E3%25252580%25252591-%25252520%252525E5%252525A5%252525BD%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%252525E5%252525B0%252525BD%252525E5%2525259C%252525A8%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A7%2521%252526linkType%25253D%26%7C%26; 51job=cenglish%3D0%26%7C%26' \
  --compressed"""
data = select_table('select jobid,job_href from test1')
print(type(data))
for result in data:
    time.sleep(0.5)
    job_href = result["job_href"]
    jobid = result["jobid"]
    a = url2.format(job_href)
    print(a)
    detail = subprocess.run(a, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    detailInfo = ""
    if detail.returncode == 0:
        print("请求成功")
        detailInfo = my_decode(detail.stdout)
    else:
        print("请求失败")
        detailInfo = my_decode(detail.stderr)
    print(detailInfo)
    soup = BeautifulSoup(detailInfo, 'lxml')
    div = soup.find('div', class_='bmsg job_msg inbox')
    if div is None:
        continue
    txt = get_content_between_tables(div, soup.find('div', class_='mt10')).replace('\n', '').replace('\r', '').replace('\'', '')
    print(txt)
    sql = u"""insert into comp_detail VALUES ('%s' , '%s')""" % (str(jobid), str(txt))
    print(sql)
    __insert__(sql, "comp_detail")
