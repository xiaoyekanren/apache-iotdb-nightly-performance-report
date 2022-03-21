# -*- coding: utf-8 -*-
# @Time : 2022/3/9 20:15
# @Author : 李凯
# @File : main.py
# @Software: PyCharm 
# @Function: 主要控制

from lib.tools import read_txt, print_result, save_result_to_db
from src.main_configurations import parse_main_configurations
from src.matrix import parse_matrix


def main(benchmark_log, db_path):
    # 1.用户输入文本地址
    txt_path = benchmark_log
    # 2.读取文件内容
    data = read_txt(txt_path)
    # 3. 解析Main Configurations内容
    main_configurations_json = parse_main_configurations(data)
    # 4.解析Matrix
    matrix_json = parse_matrix(data)
    # 5. 规范化打印
    print_result(main_configurations_json, matrix_json)
    # 6. 同步到存入数据库
    save_result_to_db(main_configurations_json, matrix_json, db_path)
