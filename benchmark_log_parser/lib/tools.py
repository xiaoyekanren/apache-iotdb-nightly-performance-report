# -*- coding: utf-8 -*-
# @Time : 2022/3/9 20:15
# @Author : 李凯
# @File : tools.py
# @Software: PyCharm 
# @Function: 通用工具函数

import json

from db.db import insert_db, select_db


def read_txt(txt_path):
    """
    读取文件
    :param txt_path: 文件路径
    :return:
    """
    with open(txt_path, "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        return data


def user_input():
    txt_path = input("输入解析文件地址:")
    return txt_path


def get_new_matrix_list(matrix_list):
    """
    去除空白字符
    :param matrix_list:
    :return:
    """
    matrix_list_new = []
    for matrix in matrix_list[0].split(' ')[1:]:
        if matrix != '':
            matrix_list_new.append(matrix)
    for matrix in matrix_list[1].split(' ')[1:]:
        if matrix != '':
            matrix_list_new.append(matrix)
    return matrix_list_new


def print_result(main_configurations_json, matrix_json):
    """
    打印解析内容
    :param main_configurations_json:
    :param matrix_json:
    :return:
    """
    print("\nMain Configurations解析内容为：\n" + json.dumps(main_configurations_json, ensure_ascii=False) + "\n")
    print("Result Matrix和Latency (ms) Matrix解析内容为：\n" + json.dumps(matrix_json, ensure_ascii=False) + "\n")


def save_result_to_db(main_configurations_json, matrix_json):
    """
    保存main_configurations_json
    :param main_configurations_json:
    :param matrix_json:
    :return:
    """
    java_version = read_txt('_java_version')
    datetime_timestamp = read_txt('_datetime_timestamp')
    datetime_date = read_txt('_datetime_date')
    iotdb_commit = read_txt('_iotdb_commit')
    benchmark_commit = read_txt('_benchmark_commit')
    iotdb_branch = read_txt('_iotdb_branch')

    key_name = ','.join(list(main_configurations_json.keys()))
    value_name = "','".join(list(main_configurations_json.values()))
    # main_configurations_sql = "INSERT INTO LOG({}) VALUES ({})".format(key_name, "'" + value_name + "'")
    main_configurations_sql = f"INSERT INTO LOG({key_name},_JAVA_VERSION,_TEST_BEGINNING_TIME,_BENCHMARK_COMMIT_ID,_IOTDB_COMMIT_ID,_IOTDB_BRANCH) VALUES ('{value_name},{java_version},{datetime_timestamp},{benchmark_commit}),{iotdb_commit},{iotdb_branch}')"
    insert_db(main_configurations_sql)
    select_id_sql = 'SELECT MAX(LOGID) FROM LOG'
    logid = select_db(select_id_sql)[0]

    for table_name in matrix_json.keys():
        value_list = matrix_json[table_name]
        matrix_value_name = "','".join(value_list)
        matrix_sql = "INSERT INTO {}(okOperation,okPoint,failOperation,failPoint,throughput,AVG,MIN,P10,P25,MEDIAN,P75,P90,P95,P99,P999,MAX,SLOWEST_THREAD,LOGID) VALUES ({})".format(
            table_name, "'" + matrix_value_name + "','" + str(logid) + "'")
        insert_db(matrix_sql)

    print("已将信息同步到数据库")
