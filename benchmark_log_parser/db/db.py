# -*- coding: utf-8 -*-
# @Time : 2022/3/9 20:14
# @Author : 李凯
# @File : db.py
# @Software: PyCharm 
# @Function: 数据库操作

import sqlite3

from config.settings import DB_PATH


def insert_db(sql, db_path):
    conn = sqlite3.connect(db_path)  # 打开或创建数据库文件
    c = conn.cursor()  # 获取游标
    c.execute(sql)
    conn.commit()  # 提交数据库操作
    conn.close()  # 关闭数据库连接


def select_db(sql):
    conn = sqlite3.connect(DB_PATH)  # 打开或创建数据库文件
    c = conn.cursor()  # 获取游标
    row = c.execute(sql)
    res = row.fetchone()
    conn.commit()  # 提交数据库操作
    conn.close()  # 关闭数据库连接
    return res
