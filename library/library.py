import numpy as np

def read_file(file_name):
    f = open(file_name, 'r').read().split()
    f = np.asarray(f)
    lines = len(open(file_name).readlines())
    f = f.reshape(lines, int(len(f)/lines))
    return f
    
def write_file(file_name):

    return open(file_name, 'a')
    
def date_format_transform(date):
    date_new = ''
    for i in date:
        if i == '-':
            date_new += '/'
        else:
            date_new += i
    return date_new