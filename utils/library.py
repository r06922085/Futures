import numpy as np
from datetime import date as date_time
import datetime


class utils():
    def read_file(self, file_name):
        f = open(file_name, 'r').read().split()
        f = np.asarray(f)
        lines = len(open(file_name).readlines())
        f = f.reshape(lines, int(len(f)/lines))
        return f

    def get_today(self):
        '''
        Return what day is it,
        if it's still before 4 pm,
        the data has not come out yet, 
        so we set the day to the yesterday
        '''
        today_hour = datetime.datetime.now().timetuple().tm_hour
        
        if today_hour < 16:
            today = str(date_time.today() - datetime.timedelta(1))
        else:
            today = str(date_time.today())

        today = today.replace("-", "/")

        return today

    def date_format_transform(self, date):
        return date.replace("-", "/")
        date_new = ''
        for i in date:
            if i == '-':
                date_new += '/'
            e
