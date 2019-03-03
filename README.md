# My research on Futures
# 期貨的研究

## What is this?
此研究專於分析如何預測期貨走勢.
透過期交所批露資料(例如:三大法人每日交易口數)預測未來一天期貨漲跌,起因於台股期貨於2017年開放期貨的下午盤交易,開盤時間為下午三點,而期交所於每日下午兩點批露當日上午的各項交易資訊,因此希望能夠基於兩點時的紕漏資料預測下意天的期貨走勢,並於三點進行買賣.

## Training Data
->2008-2012三大法人交易資訊
->2015-2019(today)三大法人交易資訊
來源: 2008-2012是跟期交所買的,而2015之後是用爬蟲程式在期交所網站抓下來的

## Prerequisites
-Python: 3.6.6

-Tensorflow: 1.11.0

-Cuda: v9.0

## Result

## Running
To renew the recent data:
--python renew_data.py

To to analyze the data:
--python main.py --policy_1 x --policy_2 y

To analyze the data with my main policy:
--python main.py --look

## Author
-Liocean: https://github.com/r06922085
