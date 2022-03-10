# -*- coding: utf-8 -*-
# @Time : 2022/3/9 20:15
# @Author : 李凯
# @File : main_configurations.py
# @Software: PyCharm 
# @Function: 解析main configurations

import re


def parse_main_configurations(data):
    regex_str = re.compile(".+=.+", re.M)
    col_list = regex_str.findall(data)[1:]
    main_configurations_json = {}
    for col in col_list:
        col_new = col.strip()
        if col_new.split('=')[1]:
            main_configurations_json[col_new.split('=')[0]] = col_new.split('=')[1]
    return main_configurations_json
