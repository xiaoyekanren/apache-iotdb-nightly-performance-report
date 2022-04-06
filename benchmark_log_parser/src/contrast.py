# coding=utf-8
import sys
import sqlite3


def select_db_all(sql, db_path):
    conn = sqlite3.connect(db_path)  # 打开或创建数据库文件
    c = conn.cursor()  # 获取游标
    row = c.execute(sql)
    res = row.fetchall()
    conn.commit()  # 提交数据库操作
    conn.close()  # 关闭数据库连接
    return res


def main(db_path, iotdb_branch, java_version, value):
    sql = f'select INGESTION.throughput,INGESTION.AVG from INGESTION,log where INGESTION.LOGID=log.LOGID and log._IOTDB_BRANCH="{iotdb_branch}" and log._JAVA_VERSION="{java_version}" order by id desc limit 2;'
    cur_line, last_line = select_db_all(sql, db_path)
    if value == 'cur_throught':
        print(cur_line[0])
    elif value == 'cur_avg':
        print(cur_line[1])
    elif value == 'last_throught':
        print(last_line[0])
    elif value == 'last_avg':
        print(last_line[1])


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
