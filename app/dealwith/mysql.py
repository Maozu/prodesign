import pymysql

# return (
#   id:shenfenzhenghao
# 	name:xxx
# 	sex:male
# 	nation:han
# 	bith:xxxxxx
# 	height:xxx
# 	characteristic:xxx
# 	location:xxx
# 	)

import pymysql


def create():
    conn = pymysql.connect(host='114.67.242.13', user='root', password='1234', database='person_info', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS info")
    sql = """create table info(
    id char(20) PRIMARY KEY,
    name char(20),
    sex char(10),
    nation char(30),
    birth char(30),
    height char(10),
    characteristic char(255),
    location char(255))"""
    cursor.execute(sql)
    cursor.close()
    conn.close()


def select(id):
    conn = pymysql.connect(host='114.67.242.13', user='root', password='1234', database='person_info', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select *from info where id like '%%%s%%'" % id)
    rs = cursor.fetchone()
    print("这是rs哦")
    cursor.close()
    conn.close()
    if rs is None:
        return "请你检查一下数据库哦"
    else:
        return rs

# value[(),()]
def insert(values):
    conn = pymysql.connect(host='114.67.242.13', user='root', password='1234', database='person_info', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO info(id,name,sex,nation,birth,height,characteristic,location) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql, values)
        conn.commit()
        print('插入数据成功')
    except:
        conn.rollback()
        print("插入数据失败")
    cursor.close()
    conn.close()


def create():
    conn = pymysql.connect(host='114.67.242.13', user='root', password='1234', database='person_info', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS info")

    sql = """create table info(
    id char(20) PRIMARY KEY,
    name char(20),
    sex char(10),
    nation char(30),
    birth char(30),
    height char(10),
    characteristic char(255),
    location char(255))"""

    cursor.execute(sql)
    conn.close()




# values=[("1","2","3","4","5","6","7","8")]
# for i in values:
#     insert(i)