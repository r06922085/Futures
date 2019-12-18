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

        self.get_data()

    def get_data(self):
        last_day = self.f[-1][0]

        require_day = self.get_next_day(last_day)

        today = self.util.get_today()

        while True:
            if require_day > today:
                break
            print(require_day)
            payload = self.get_payload(require_day)
            reup = self.request(payload)
            self.write(reup, require_day)
            require_day = self.get_next_day(require_day)
        print('The data has been update to the latest day!')

    def write(self, reup, require_day):
        if len(reup) == 0:
            return
        self.val = reup[164].text.replace('\n', '').replace('\t', '').replace('\r', '').replace(',', '')

        self.fw.write(require_day)
        self.fw.write('  ')
        self.fw.write(str(self.val))
        self.fw.write('\n')

    def request(self, payload):
        res = requests.post(
            "https://www.taifex.com.tw/cht/3/futContractsDate", data=payload)
        res.encoding = 'utf8'
        soup = BeautifulSoup(res.text, "lxml")
        reup = soup.select('tr[class="12bk"] td div')

        return reup

    def get_payload(self, day):
        payload = {
            'queryType': '1',
            'goDay': '',
            'doQuery': '1',
            'dateaddcnt': '1',
            'queryDate': day,
            'commodityId': 'TXF'
        }

        return payload

    def get_next_day(self, day):
        yy, mm, dd = day.split('/')
        today = datetime.date(int(yy), int(mm), int(dd))
        tommorrow = today + datetime.timedelta(days=1)
        tommorrow = str(tommorrow).replace('-', '/')

        return tommorrow


if __name__ == '__main__':
    s = scrapt_legal()
