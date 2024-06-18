import pymysql

def Connect():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='crypto'
    )
    return conn