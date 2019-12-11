import datetime
import requests
from bs4 import BeautifulSoup

from utils.library import utils


class scrapt_legal():
    def __init__(self):
        self.util = utils()

        self.file_name = 'data/legal_2015_.txt'
        self.f = self.util.read_file(self.file_name)
        self.fw = open(self.file_name, 'a')
        self.last_day = self.f[-1][0]
        self.get_data()
        print('The data has been update to the latest day!')

    def get_data(self):
        # set time information

        date = self.last_day

        today = self.util.get_today()

        yy, mm, dd = self.get_date_detail(str(date))

        print(today)
        # while True:
        #     if date == today:
        #         break

        #     payload_price = self.get_payload_price(dd, mm, yy, date)

        #     reup = self.request(payload_price)

        #     yy, mm, dd, date = self.renew_dates(yy, mm, dd)

        #     if len(reup) > 0:
        #         print(date)

        #         self.val = np.array((reup[9].text).split('\n'))
        #         self.val = self.val[24].replace(',', '')
        #         self.val = int(self.val)
        #         print(self.val)
        #         #self.val = int(self.val[-1].replace(',',''))
        #         self.write_txt(date)

    def write_txt(self, date):
        print('writting...')
        self.fw.write(date)
        self.fw.write('  ')
        self.fw.write(str(self.val))
        self.fw.write('\n')

    def request(self, payload_price):
        res = requests.post(
            "https://www.taifex.com.tw/cht/3/futContractsDate", data=payload_price)
        res.encoding = 'utf8'
        soup = BeautifulSoup(res.text, "lxml")
        reup = soup.select('tr[class="12bk"] td div')
        print(reup[9].text)
        return reup

    def get_payload_price(self, dd, mm, yy, date):
        print(date)
        payload = {
            'queryType': '3',
            'goDay': '',
            'doQuery': '1',
            'dateaddcnt': '1',
            'queryDate': date,
            'commodityId': 'TXF'
        }
        print(payload)

        return payload

    def renew_dates(self, yy, mm, dd):
        now = datetime.date(int(yy), int(mm), int(dd))
        date = now + datetime.timedelta(days=1)
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
                break
            elif i == '/' or i == '-':
                stage = stage + 1
            if i != '/' and i != '-':
                if stage == 1:
                    yy = yy + i
                elif stage == 2:
                    mm = mm + i
                elif stage == 3:
                    dd = dd + i
        return yy, mm, dd


if __name__ == '__main__':
    s = scrapt_legal()
