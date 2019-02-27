import argparse
import numpy as np
from Policy import policy
from library.library import *
import matplotlib.pyplot as plt

class main():
    def parse(self):
        parser = argparse.ArgumentParser(description="MLDS 2018 HW4")
        parser.add_argument('--policy_1', default=None, help='data type')
        parser.add_argument('--policy_2', default=None, help='data type')
        parser.add_argument('--look', action='store_true', help='set to the main policy')
        
        try:
            from argument import add_arguments
            parser = add_arguments(parser)
        except:
            pass
        args = parser.parse_args()
        return args

    def run(self, args):
        agent = policy(args)
        return agent
       
    def analyze(self, agent, file_name):
        self.renew_data()
        
        data = read_file(file_name)
        price = read_file('data/price_2008_.txt')
        price = self.set_bias(data, price) 
        
        total_earn = 0
        worst_lose = 0
        max_earn = 0
        last_peak = 0
        last_decision = -1
        count_type = 1
        total_earn_record = []
        earn_record = []
        loss_record = []
        last_peak_record = []
        lasting_record = []
        lasting = 0
        
        for i in range(len(data)):
            decision = agent.decide(price, data, i, (max_earn-total_earn))
            if last_decision == decision:
                if decision == 1:
                    lasting += 1
                elif decision == -1:
                    lasting -= 1
                else:
                    lasting = 0
            else:
                if decision == 1:
                    lasting = 1
                elif decision == -1:
                    lasting = -1
                else:
                    lasting = 0
            total_earn += self.count(price, i, decision, count_type)
            if max_earn < total_earn:
                last_peak = 0
            else:
                last_peak += 1
            
            max_earn = max(max_earn , total_earn)
            worst_lose = min((total_earn-max_earn) , worst_lose)
            total_earn_record.append(total_earn)
            earn_record.append(self.count(price, i, decision, count_type))
            loss_record.append(max_earn-total_earn)
            last_peak_record.append(last_peak)
            lasting_record.append(lasting)
            last_decision = decision
        
        print(file_name, ': ', 
              'total_earn: ', total_earn,
              'worst_lose: ', worst_lose)
        self.paint(loss_record, total_earn_record)
            
    def count(self, price, i, decision, type):
        if type == 1:
            if i >= (len(price)-1):
                return 0
            if price[i][1] == price[i+1][1]:
                if decision == 1:
                    return int(price[i+1][3]) - int(price[i][3])
                elif decision == -1:
                    return int(price[i][3]) - int(price[i+1][3])
                elif decision == 0:
                    return 0
            elif price[i][1] != price[i+1][1]:
                if decision == 1:
                    return int(price[i+1][3]) - int(price[i][6])
                elif decision == -1:
                    return int(price[i][6]) - int(price[i+1][3])
                elif decision == 0:
                    return 0
        elif type == 2:
            if i >= (len(price)-1):
                return 0
            if price[i][1] == price[i+1][1]:
                if decision == 1:
                    if price[i+1][2] >= price[i][3]:
                        return int(price[i+1][3]) - int(price[i][3])
                    else:
                        return int(price[i+1][2]) - int(price[i][3])
                elif decision == -1:
                    if price[i+1][2] >= price[i][3]:
                        return int(price[i][3]) - int(price[i+1][2])
                    else:
                        return int(price[i][3]) - int(price[i+1][3])
                elif decision == 0:
                    return 0
            elif price[i][1] != price[i+1][1]:
                if decision == 1:
                    if price[i+1][2] >= price[i][6]:
                        return int(price[i+1][3]) - int(price[i][6])
                    else:
                        return int(price[i+1][2]) - int(price[i][6])
                elif decision == -1:
                    if price[i+1][2] >= price[i][6]:
                        return int(price[i][6]) - int(price[i+1][2])
                    else:
                        return int(price[i][6]) - int(price[i+1][3])
                elif decision == 0:
                    return 0
                    
        elif type == 3:
            if i >= (len(price)-1):
                return 0
            if price[i][1] == price[i+1][1]:
                if decision == 1:
                    if price[i+1][2] <= price[i][3]:
                        return int(price[i+1][3]) - int(price[i][3])
                    else:
                        return int(price[i+1][2]) - int(price[i][3])
                elif decision == -1:
                    if price[i+1][2] <= price[i][3]:
                        return int(price[i][3]) - int(price[i+1][2])
                    else:
                        return int(price[i][3]) - int(price[i+1][3])
                elif decision == 0:
                    return 0
            elif price[i][1] != price[i+1][1]:
                if decision == 1:
                    if price[i+1][2] <= price[i][6]:
                        return int(price[i+1][3]) - int(price[i][6])
                    else:
                        return int(price[i+1][2]) - int(price[i][6])
                elif decision == -1:
                    if price[i+1][2] <= price[i][6]:
                        return int(price[i][6]) - int(price[i+1][2])
                    else:
                        return int(price[i][6]) - int(price[i+1][3])
                elif decision == 0:
                    return 0
        
    
    def get_data(self, file_name):
        data = open(file_name, 'r').read().split()
        lines = len(open(file_name, 'r').readlines())
        data = np.reshape(data,(lines,int(len(data)/lines))) 
        return data
        
    def set_bias(self, data, price):
        for i in range(len(price)):
            if price[i][0] == data[0][0]:
                price_new = price[i:i+len(data)]
                return price_new
        
        print('can not find the bias') 
        return price  
        
    def paint(self, plt1, plt2):
        fig = plt.figure()
        ax1 = fig.add_subplot(2,1,1)
        ax2 = fig.add_subplot(2,1,2)
        #ax1.plot(self.total_arr)
        ax1.plot(plt1)
        ax2.plot(plt2)
        plt.show()     

    def renew_data(self):
        from scrapt_legal import scrapt_legal
        from scrapt_price import scrapt_price

        scrapt_legal = scrapt_legal()
        scrapt_price = scrapt_price()	
        
    
if __name__ == '__main__':
    main = main()
    args = main.parse()
    agent = main.run(args)
    main.analyze(agent, 'data/legal_2008_2012.txt')
    main.analyze(agent, 'data/legal_2015_.txt')
        