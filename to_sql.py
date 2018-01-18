# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:33:59 2018

@author: Yangzj
"""

import tushare as ts
import sys
from sqlalchemy import create_engine

def industrytodb():
    #获取sina行业分类信息
    industry_sina = ts.get_stock_basics()
    industry_sina=industry_sina.reset_index()
    
    print(industry_sina, sep=' ', end='\n', file=sys.stdout, flush=False)
    #获取申万行业分类信息
    '''industry_sw = ts.get_industry_classified("sw")
    print(industry_sw, sep=' ', end='\n', file=sys.stdout, flush=False)
   # engine = create_engine('mysql://root:123456@localhost/stockdb?charset=utf8') 
    print("连接数据库", sep=' ', end='\n', file=sys.stdout, flush=False) '''
    engine = create_engine('mysql+pymysql://root:root@localhost/test?charset=utf8')
    #print(engine, sep=' ', end='\n', file=sys.stdout, flush=False)
    # industry_sina.to_sql('industry_sina_data',engine,if_exists='append')
    # industry_sw.to_sql('industry_sw_data',engine,if_exists='append')
    industry_sina.to_sql('stock_basics',engine,if_exists='replace')
    #industry_sw.to_sql('industry_sw_data',engine)

if __name__ == '__main__':
    # 获取sina和申万行业分类信息
    industrytodb()

