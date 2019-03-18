# -*- coding: utf-8 -*-

# 2019/3/18 0018 下午 5:18     

__author__ = 'RollingBear'


import config

conf = config.config('\\config.ini')
print(conf.get('font').title_font)