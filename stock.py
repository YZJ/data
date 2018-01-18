# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 22:09:08 2018

@author: Yangzj
"""

import requests
from bs4 import BeautifulSoup
import traceback
import re

 #获得html文本
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
        
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser') 
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue    
        

def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html=="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})
 
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})
             
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
             
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write( str(infoDict) + '\n' )
                
            print(stock)
        except:
            continue        
        
def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'C:/ddup/pythonspider/BaiduStockInfo.txt'
    slist=[]
    getStockList(slist, stock_list_url)
    
    #print(slist)
    getStockInfo(slist, stock_info_url, output_file)        
    
main()    