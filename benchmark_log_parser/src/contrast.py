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


def main(value, db_path):
    cur_line, last_line = select_db_all('select * from INGESTION order by id desc limit 2', db_path)
    if value == 'cur_throught':
        print(cur_line[6])
    elif value == 'cur_avg':
        print(cur_line[7])
    elif value == 'last_throught':
        print(last_line[6])
    elif value == 'last_avg':
        print(last_line[7])


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
