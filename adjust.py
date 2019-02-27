import numpy as np
from library.library import *
class adjust(object):
    def __init__(self):
        data = read_file('data/legal_2015_2018.txt')
        price = read_file('data/price_2008_2018.txt')
        writer = write_file('data/legal_2015_2018_new.txt')
        for i in range(len(data)):
            writer.write(price[i+1712][0])
            writer.write('  ')
            writer.write(data[i][1])
            writer.write('\n')
            
       
    def transform(self, date):
        strs = ''
        
        for i in range(len(date)):
            
            if i == 4 or i == 6:
                strs += '/'
            else:
                strs += date[i]
        print(strs)
        return str(strs)
    
if __name__ == '__main__':
    s = adjust()