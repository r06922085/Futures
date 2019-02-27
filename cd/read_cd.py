global f

global fw
fw = open('legal_temp.txt', 'a')

global fbd
fbd = open('big_deal.txt','r')
s = fbd.read()
fbd_data = s.split()

mnoth = 47
cur_year = "2008"
cur_month = "03"
count = 0
for mon in range(0,mnoth):
    file_name = "WBOIVL3F_"
    yy = int(cur_year)
    mm = int(cur_month)
    cur_year = ""
    cur_month = ""
    mm = mm + 1
    if mm == 13:
        yy = yy + 1
        mm = 1
    if mm < 10:
        cur_month = "0"
    cur_year = str(yy)
    cur_month = cur_month + str(mm)
    file_name = file_name + cur_year + cur_month + '.txt'
    
    f = open(file_name,'r')
    s = f.read()
    data = s.split()
        
    for i in range(0,int(len(data)/16)):
        name = data[16*i+1]
        type = data[16*i+3]
        value = 0
        date = ""
        if name == "臺股期貨" and type == "A":
            value = int(data[16*i+14]) + int(data[16*(i+1)+14]) + int(data[16*(i+2)+14])
            date = data[16*i+0]
            fw.write(date)
            fw.write('   ')
            fw.write(str(value))
            fw.write('   ')
            fw.write(fbd_data[(count+929)*14+10])
            fw.write('   ')
            fw.write(fbd_data[(count+929)*14+11])
            fw.write('   ')
            fw.write(fbd_data[(count+929)*14+12])
            fw.write('   ')
            fw.write(fbd_data[(count+929)*14+13])
            fw.write('\n')
            count = count +1 
    
    
print(count)
