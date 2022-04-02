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


if __name__ == '__main__':
    # for i in select_db_all('SELECT INGESTION.throughput from INGESTION,log where INGESTION.LOGID=log.LOGID and log._IOTDB_BRANCH="rel/0.12";', '/Users/zhangzhengming/Src/Python/benchmark.db'):
    #     print(str(i).replace(',', '').replace('(', '').replace(')', ''))
    for i in select_db_all('select INGESTION.throughput,INGESTION.AVG from INGESTION,log where INGESTION.LOGID=log.LOGID and log._IOTDB_BRANCH="rel/0.12" and log._JAVA_VERSION like "1.8" order by id desc limit 2', '/Users/zhangzhengming/Src/Python/benchmark.db'):
        print(i)
