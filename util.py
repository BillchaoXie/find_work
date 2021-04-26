# _*_coding:utf-8_*_
# author: xc
# date: 2021-02-20
import pymysql.cursors
from bs4 import BeautifulSoup
import bs4
def my_decode(value):
    try:
        msg = value.decode("utf-8")
    except Exception as e:
        msg = value.decode("gbk")
    except:
        msg = "unknow, {}".format(value)
    finally:
        return msg




connection = pymysql.connect(host='172.17.137.65',
                                 port=3306,
                                 user='search_for_xc',
                                 passwd='1#hx6Qbr',
                                 db='search',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
#查询表数据
def select_table(sql):
    try:
        with connection.cursor() as cursor:
             cursor.execute(sql)
             data = cursor.fetchall()
             print(data)
        return data
    finally:
        connection.close()

# 根据元组数据生成mysql语句
def make_sql(tuple2, table_name):
    str1 = "CREATE TABLE `%s`" % (table_name)
    str2 = "ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    str4 = ""
    for i in tuple2:
        str3 = "`" + i + "`" + " " + "varchar(255) DEFAULT NULL,"
        str4 = str4 + str3
    str5 = "(" + str4.rstrip(",") + ")"
    str6 = str1 + " " + str5 + str2
    return str6


# 数据插入函数
def create(sql, table_name):
    conn = pymysql.connect(host='172.17.137.65',
                                 port=3306,
                                 user='search_for_xc',
                                 passwd='1#hx6Qbr',
                                 db='search',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:

        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit()
        print(u"创建表%s成功" % (table_name))
    finally:
        conn.close()

def __insert__(sql, table_name):
    conn = pymysql.connect(host='172.17.137.65',
                                 port=3306,
                                 user='search_for_xc',
                                 passwd='1#hx6Qbr',
                                 db='search',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
        conn.commit()
        print(u"插入表%s成功" % (table_name))
    finally:
        conn.close()



# 把字典数据转化为元组数据
def tuple1(dict1):
    list1 = []
    print(u"总字段数:" + str(len(dict1)))
    for i in dict1.keys():
        list1.append(i)
    m = tuple(list1)
    return m

def __create__table(table_name, dict1):
    create(make_sql(tuple1(dict1), table_name), table_name)





def InsertData(TableName, dic):
        conn  = pymysql.connect(host='172.17.137.65',
                                 port=3306,
                                 user='search_for_xc',
                                 passwd='1#hx6Qbr',
                                 db='search',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
        COLstr = ''  # 列的字段
        ROWstr = ''  # 行字段

        ColumnStyle = ' VARCHAR(255)'
        for key in dic.keys():
            COLstr = COLstr + ' ' + key + ColumnStyle + ','
            ROWstr = (ROWstr + '"%s"' + ',') % (dic[key])

        # 推断表是否存在，存在运行try。不存在运行except新建表，再insert
        # print("CREATE TABLE if not exists %s (%s)" % (TableName, COLstr[:-1]))
        # print("INSERT INTO %s VALUES (%s)" % (TableName, ROWstr[:-1]))
        cur.execute("CREATE TABLE if not exists %s (%s)" % (TableName, COLstr[:-1]))
        cur.execute("INSERT INTO %s VALUES (%s)" % (TableName, ROWstr[:-1]))
        conn.commit()
        cur.close()
        conn.close()

def is_child(child, father):
    if child in father:
        return True
    seek_list = father.contents
    for i in seek_list:
        if isinstance(i, bs4.element.NavigableString):
            pass
        elif child in i:
            return True
        else:
            flag = is_child(child, i)
            if flag == True:
                return True
    return False

def get_content_between_tables(pre, nxt):
    #如果第二个table在第一个里面
    txt = ""
    if is_child(nxt, pre):
        cur = pre.next_element
        while cur != nxt and cur is not None:
            if isinstance(cur, bs4.element.NavigableString):
                txt += cur
            cur = cur.next_element
    #类似并列关系
    else:
        #先找到pre结束的下一个元素
        cur = pre.next_element
        while is_child(cur, pre):
            cur = cur.next_element
        #获取内容
        while cur != nxt and cur is not None:
            if isinstance(cur, bs4.element.NavigableString):
                txt += cur
            cur = cur.next_element
    return txt