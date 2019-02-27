class policy():
    def __init__(self, args_):
        self.args = args_
        
        self.last_lasting_day = 0
        self.last_decision =  0
        self.lasting_day = 0
        
        
        
    def decide(self, price, data, i, loss):
        self.data = data
        self.price = price
        self.i = i
        self.loss = loss
        
        if self.args.look:
            self.args.policy_1 = 1
            self.args.policy_2 = 1
        
        decision_1 =  self.policy_1(int(self.args.policy_1), i)
        return self.policy_2(int(self.args.policy_2), decision_1)
    
    def policy_1(self, policy, i):    
        if policy == 1:
            if i < 1 :
                return 0
            price = self.get_price(i)
            val = self.get_val(i)
            if val['tod'] > val['yes'] and val['tod'] > 0:
                return 1
            elif val['tod'] < val['yes'] and val['tod'] < 0:
                return -1
            else:
                return 0
                
                
    def policy_2(self, policy, decision):
        if policy == 1:
            return decision
         
        if policy == 2:
            if self.last_decision*decision > 0:
                self.lasting_day += 1
            elif self.last_decision*decision < 0:
                self.last_lasting_day = self.lasting_day
                self.lasting_day = 0
            else:
                self.lasting_day = 1
            
            self.last_decision = decision
            
            if self.lasting_day == 1:
                if self.last_lasting_day == 1:
                    return 0
                else:
                    return decision
            else:
                return decision
                
        if policy == 3:
            if decision * self.last_decision == -1:
                d = 0
            else:
                d = decision
            
            self.last_decision = decision
            return d
                
            
                
    
            
    def get_price(self, i):
        if self.price[i][1] == self.price[i-1][1]:
            yes_start = self.price[i-1][2]
            yes_end = self.price[i-1][3]
            tod_start = self.price[i][2]
            tod_end = self.price[i][3]
        else:
            yes_start = self.price[i-1][5]
            yes_end = self.price[i-1][6]
            tod_start = self.price[i][2]
            tod_end = self.price[i][3]
        price={'yes_start' : yes_start,
               'yes_end' : yes_end,
               'tod_start' : tod_start,
               'tod_end' : tod_end}
        return price
    def get_val(self, i):
        if i < 1:
            tof_val = 0
        else:
            tod_val = int(self.data[i][1])
        if i < 2:
            yes_val = 0
        else:
            yes_val = int(self.data[i-1][1])
        if i < 3:
            bef_val = 0
        else:
            bef_val = int(self.data[i-2][1])
            
        val = {'tod' : tod_val,
               'yes' : yes_val,
               'bef' : bef_val}
        return val
        
                    