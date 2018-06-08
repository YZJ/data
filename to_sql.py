# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:33:59 2018

@author: Yangzj
"""
  
import tushare as ts
import sys
from sqlalchemy import create_engine

def getReportData(year,quarter,engine):
#获取2017年第4季度的业绩报表数据
    try:
        date = tostr(year,quarter)
        report_data=ts.get_report_data(year,quarter)
        report_data=report_data.reset_index()
        report_data['date']=date
        report_data.to_sql('report_data',engine,if_exists='append')
        print('report_data')
    except:
        print('report_data excpet')

def getOperationData (year,quarter,engine) :
            #获取2017年第4季度的营运能力数据
    try:
        date = tostr(year,quarter)
        operation_data = ts.get_operation_data(year,quarter)
        operation_data =operation_data.reset_index()
        operation_data['date']=date
        operation_data.to_sql('operation_data',engine,if_exists='append')
        print('operation_data')
    except:
        print('operation_data excpet')
        
def getGrowthData(year,quarter,engine):
        #获取2017年第4季度的成长能力数据
    try:
        date = tostr(year,quarter)
        growth_data = ts.get_growth_data(year,quarter)
        growth_data =growth_data.reset_index()
        growth_data['date']=date
        growth_data.to_sql('growth_data',engine,if_exists='append')
        print('growth_data')        
    except:
        print('growth_data error')
        
def getDebtpayingData(year,quarter,engine):
        #获取2017年第4季度的偿债能力数据
    try:
        date = tostr(year,quarter)
        debtpaying_data = ts.get_debtpaying_data(year,quarter)
        debtpaying_data =debtpaying_data.reset_index()
        debtpaying_data['date']=date
        debtpaying_data.to_sql('debtpaying_data',engine,if_exists='append')
        print('debtpaying_data') 
    except:
        print('debtpaying_data error')
        
def getCashFlow(year,quarter,engine):
        #获取2017年第4季度的现金流量数据
    try:
        date = tostr(year,quarter)
        cashflow_data = ts.get_cashflow_data(year,quarter)
        cashflow_data =cashflow_data.reset_index()
        cashflow_data['date']=date
        cashflow_data.to_sql('cashflow_data',engine,if_exists='append')
        print('cashflow_data')        
    except:
        print('cashflow_data error')
        
def getProfitData(year,quarter,engine):
        #获取2017年第4季度的盈利能力数据
    try:
        date = tostr(year,quarter)
        profit_data = ts.get_profit_data(year,quarter)
        profit_data =profit_data.reset_index()
        profit_data['date']=date
        profit_data.to_sql('profit_data',engine,if_exists='append')
        print('profit_data')      
    except:
        print('profit_data error')        

def tostr(year,quarter):
    date = '%d%d' % (year,quarter)
    return date
    
def datatodb():
    
    
    year = 2017
    quarter = 1
    while quarter <4:
    
       
        #创建连接数据库test引擎
        engine = create_engine('mysql+pymysql://root:root@localhost/test?charset=utf8')
        
        '''
        #获取沪深上市公司基本信息
        stock_basics = ts.get_stock_basics()
        stock_basics = stock_basics.reset_index()
        stock_basics.to_sql('stock_basics',engine,if_exists='append')
        print('stock_basics')
        '''
        
        getReportData(year,quarter,engine)
        
        getOperationData (year,quarter,engine)

        getGrowthData(year,quarter,engine)

        getDebtpayingData(year,quarter,engine)
        
        getCashFlow(year,quarter,engine)

        getProfitData(year,quarter,engine)
        
        quarter += 1

    
    
if __name__ == '__main__':
    
    datatodb()

