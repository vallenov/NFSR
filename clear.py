import shutil
import os

def clear_way(dir):
    '''Clear directory'''
    for directory in os.listdir(dir):
        for file in os.listdir(dir+'\\'+directory):
            shutil.rmtree(dir+'\\'+directory+'\\'+file)
    try:
        err = open('error.log', 'w')
        move = open('move.log', 'w')
    except FileNotFoundError:
        print('File not found!')
    else:
        print('Clear log files done')
    print('Clear {} done'.format(dir))

clear_way(r'C:\Prog\Python\NFSR\receive')
clear_way(r'C:\Prog\Python\NFSR\storage')