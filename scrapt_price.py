##抓取2008~的期貨開、收盤價
import requests
import re
import datetime
from bs4 import BeautifulSoup
from array import array
from datetime import date as date_time
from library.library import *

class scrapt_price(object):
    def __init__(self):
        global f
        self.f = read_file('data/price_2008_.txt')
        self.fw = write_file('data/price_2008_.txt')
        self.last_day = self.f[-1][0]
        self.get_price()
        print('The data has been update to the latest day!')
    def get_price(self): 
        date = self.last_day
        
        today_hour = datetime.datetime.now().timetuple().tm_hour
        
        if today_hour < 16:
            today = date_format_transform(str(date_time.today()- datetime.timedelta(1)))
        else:
            today = date_format_transform(str(date_time.today()))
            
        yy, mm, dd = self.get_date_detail(str(date))
        
        while True:
            if date == today:
                break;
            
            payload_price = self.get_payload_price(dd, mm, yy, date)
            
            reup_price = self.request(payload_price)
            
            yy, mm, dd, date = self.renew_dates(yy, mm, dd)
            
            if len(reup_price) > 0:
                print(date)
                self.e_1 = str(int(reup_price[1].text))
                self.e_1_p = str(int(reup_price[2].text))
                self.e_1_pp = str(int(reup_price[5].text))
                self.e_2 = str(int(reup_price[16].text))
                self.e_2_p = str(int(reup_price[17].text))
                self.e_2_pp = str(int(reup_price[20].text))
                self.write_txt(date)
            
            
                
    def write_txt(self, date):
        print('writting...')
        self.fw.write(date)
        self.fw.write('  ')
        self.fw.write(str(self.e_1))
        self.fw.write('  ')
        self.fw.write(str(self.e_1_p))
        self.fw.write('  ')
        self.fw.write(str(self.e_1_pp))
        self.fw.write('  ')
        self.fw.write(str(self.e_2))
        self.fw.write('  ')
        self.fw.write(str(self.e_2_p))
        self.fw.write('  ')
        self.fw.write(str(self.e_2_pp))
        self.fw.write('\n')
    def request(self, payload_price):
        res_price = requests.post("http://www.taifex.com.tw/cht/3/futDailyMarketReport",data = payload_price)
        soup_price = BeautifulSoup(res_price.text,"html.parser")
        reup_price = soup_price.select('.12bk')
        return reup_price
    def get_payload_price(sel, dd, mm, yy, date):
        payload_price = {
            'queryType': '3',
            'marketCode': '0',
            'dateaddcnt': '1',
            'commodity_id': 'TX',
            'commodity_id2': '',
            'queryDate': date,
            'MarketCode': '0',
            'commodity_idt': 'TX',
            'commodity_id2t': '',
            'commodity_id2t2': ''
            }
            
        return payload_price
    def renew_dates(self, yy, mm, dd):
        now = datetime.date(int(yy),int(mm),int(dd))
        date = now + datetime.timedelta(days = 1)
        yy, mm, dd = self.get_date_detail(str(date))
        date = yy+'/'+mm+'/'+dd    
        return yy, mm, dd, date  
    def get_date_detail(self, date):
        yy = ""
        mm = ""
        dd = ""
        stage = 1
        for i in date:
            if ord(i) == 9 or ord(i) == ord('\n'):
                break;
            elif i == '/' or i == '-':
                stage = stage +1 
            if i != '/' and i != '-':    
                if stage == 1:
                    yy = yy + i
                elif stage == 2:
                    mm = mm + i
                elif stage == 3:
                    dd = dd + i;    
        return yy, mm, dd
        
if __name__ == '__main__':
    s = scrapt_price()