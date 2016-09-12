#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""html生成工具"""
from mako.template import Template
from mako.lookup import TemplateLookup


def data2html(date, data_list, directory, template):
    """数据转换成html"""

    mlookup = TemplateLookup(directories=[directory],
                             input_encoding='utf-8',
                             output_encoding='utf-8',
                             encoding_errors='replace')
    t = mlookup.get_template(template)
    html = t.render(date=date, data_list=data_list)
    return html
