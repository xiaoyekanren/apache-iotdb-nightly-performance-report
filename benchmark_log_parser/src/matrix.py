# -*- coding: utf-8 -*-
# @Time : 2022/3/9 20:16
# @Author : 李凯
# @File : matrix.py
# @Software: PyCharm 
# @Function: 解析matrix

import re

from lib.tools import get_new_matrix_list


def parse_matrix(data):
    matrix_json = {}
    regex_str_1 = re.compile("^INGESTION .+", re.M)
    regex_str_2 = re.compile("^PRECISE_POINT .+", re.M)
    regex_str_3 = re.compile("^TIME_RANGE .+", re.M)
    regex_str_4 = re.compile("^VALUE_RANGE .+", re.M)
    regex_str_5 = re.compile("^AGG_RANGE .+", re.M)
    regex_str_6 = re.compile("^AGG_VALUE .+", re.M)
    regex_str_7 = re.compile("^AGG_RANGE_VALUE .+", re.M)
    regex_str_8 = re.compile("^GROUP_BY .+", re.M)
    regex_str_9 = re.compile("^LATEST_POINT .+", re.M)
    regex_str_10 = re.compile("^RANGE_QUERY_DESC .+", re.M)
    regex_str_11 = re.compile("^VALUE_RANGE_QUERY_DESC .+", re.M)

    ingestion_list = regex_str_1.findall(data)
    precise_point_list = regex_str_2.findall(data)
    time_range_list = regex_str_3.findall(data)
    value_range_list = regex_str_4.findall(data)
    agg_range_list = regex_str_5.findall(data)
    agg_value_list = regex_str_6.findall(data)
    agg_range_value_list = regex_str_7.findall(data)
    group_by_list = regex_str_8.findall(data)
    latest_point_list = regex_str_9.findall(data)
    range_query_desc_list = regex_str_10.findall(data)
    value_range_query_desc_list = regex_str_11.findall(data)

    ingestion_list_new = get_new_matrix_list(ingestion_list)
    precise_point_list_new = get_new_matrix_list(precise_point_list)
    time_range_list_new = get_new_matrix_list(time_range_list)
    value_range_list_new = get_new_matrix_list(value_range_list)
    agg_range_list_new = get_new_matrix_list(agg_range_list)
    agg_value_list_new = get_new_matrix_list(agg_value_list)
    agg_range_value_list_new = get_new_matrix_list(agg_range_value_list)
    group_by_list_new = get_new_matrix_list(group_by_list)
    latest_point_list_new = get_new_matrix_list(latest_point_list)
    range_query_desc_list_new = get_new_matrix_list(range_query_desc_list)
    value_range_query_desc_list_new = get_new_matrix_list(value_range_query_desc_list)
    matrix_json['ingestion'] = ingestion_list_new
    matrix_json['precise_point'] = precise_point_list_new
    matrix_json['time_range'] = time_range_list_new
    matrix_json['value_range'] = value_range_list_new
    matrix_json['agg_range'] = agg_range_list_new
    matrix_json['agg_value'] = agg_value_list_new
    matrix_json['agg_range_value'] = agg_range_value_list_new
    matrix_json['group_by'] = group_by_list_new
    matrix_json['latest_point'] = latest_point_list_new
    matrix_json['range_query_desc'] = range_query_desc_list_new
    matrix_json['value_range_query_desc'] = value_range_query_desc_list_new
    return matrix_json
