#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:32:44 2020

@author: dingxuanlin
"""

import os
import pandas as pd

#建立路径 转到指定目录
os.chdir('/Users/dingxuanlin/Desktop/tool')

#读取原始数据
data_01 = pd.read_excel('每日报表.xlsx')

#进行数据排列
data_02 = pd.concat([data_01[10:13],data_01[24:27]])
data_02 = pd.concat([data_02,data_01[35:38]])

#建立新的dataframe 更改首列的文字内容
data_03 = data_02[['Unnamed: 1']]
data_03.loc[10,'Unnamed: 1'] = '01Plus'
data_03.loc[11,'Unnamed: 1'] = '01Pro'
data_03.loc[24,'Unnamed: 1'] = '02Plus'
data_03.loc[25,'Unnamed: 1'] = '02Pro'
data_03.loc[35,'Unnamed: 1'] = '03Standard'
data_03.loc[36,'Unnamed: 1'] = '03Pro'

#向新的dataframe注入数据
data_03[['订单本月','订单环比','订单本年累计']] = data_02[['Unnamed: 17','Unnamed: 18','Unnamed: 20']]
data_03[['销量目标','终端本月','终端环比','终端本年累计']] = data_02[['Unnamed: 2','Unnamed: 4','Unnamed: 5','Unnamed: 7']]
data_03[['结算本月','结算本年累计']] = data_02[['Unnamed: 9','Unnamed: 11']]
data_03[['在库','在途','未发','合计']] = data_02[['Unnamed: 12','Unnamed: 13','Unnamed: 14','Unnamed: 15']]

#添加达成率
data_03.insert(6,'终端达成率',data_03['销量目标'])
data_03.loc[12,'终端达成率'] = data_03.loc[12,'终端本月'] / data_03.loc[12,'销量目标']
data_03.loc[26,'终端达成率'] = data_03.loc[26,'终端本月'] / data_03.loc[26,'销量目标']
data_03.loc[37,'终端达成率'] = data_03.loc[37,'终端本月'] / data_03.loc[37,'销量目标']

#输出结果表格excel
data_03.to_excel('mydata.xlsx')
