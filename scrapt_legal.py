##抓取2008~的期貨開、收盤價
import requests
import re
import datetime
from datetime import date as date_time
from library.library import *
from bs4 import BeautifulSoup
from array import array


class scrapt_legal():
    def __init__(self):
        self.f = read_file('data/legal_2015_.txt')
        self.fw = write_file('data/legal_2015_.txt')
        self.last_day = self.f[-1][0]
        self.get_data()
        print('The data has been update to the latest day!')
    
    def get_data(self): 
        #set time information
     
        date = self.last_day
        today_hour = datetime.datetime.now().timetuple().tm_hour
        
        if today_hour < 16:
            today = self.date_format_transform(str(date_time.today()- datetime.timedelta(1)))
        else:
            today = self.date_format_transform(str(date_time.today()))
            
        yy, mm, dd = self.get_date_detail(str(date))
        
        while True:
            if date == today:
                break;
                
            payload_price = self.get_payload_price(dd, mm, yy, date)
            
            reup = self.request(payload_price)
            
            yy, mm, dd, date = self.renew_dates(yy, mm, dd)
            
            if len(reup) > 0:
                print(date) 
               
                self.val = np.array((reup[9].text).split('\n'))
                self.val = self.val[24].replace(',','')
                self.val = int(self.val)
                print(self.val)
                #self.val = int(self.val[-1].replace(',',''))
                self.write_txt(date)
            
    def write_txt(self, date):
        print('writting...')
        self.fw.write(date)
        self.fw.write('  ')
        self.fw.write(str(self.val))
        self.fw.write('\n')
    def request(self, payload_price):
        res = requests.post("http://www.taifex.com.tw/cht/3/futContractsDate",data = payload_price)
        res.encoding = 'utf8'
        soup = BeautifulSoup(res.text,"html.parser")
        reup = soup.select('.12bk')
        return reup
    def get_payload_price(self, dd, mm, yy, date):
        payload = {
        'queryType': '3',
        'goDay': '',
        'doQuery': '1',
        'dateaddcnt': '1',
        'queryDate': date,
        'commodityId': 'TXF'
        }
        
        return payload
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
    def date_format_transform(self, date):
        date_new = ''
        for i in date:
            if i == '-':
                date_new += '/'
            else:
                date_new += i
        return date_new
        
if __name__ == '__main__':
    s = scrap_legal()

