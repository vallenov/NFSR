import shutil
import os

def clear_way(dir):
    '''Clear directory'''
    for directory in os.listdir(dir):
        for file in os.listdir(dir+'\\'+directory):
            shutil.rmtree(dir+'\\'+directory+'\\'+file)
    print('Clear {} done'.format(dir))

clear_way(r'C:\Prog\Python\NFSR\receive')
clear_way(r'C:\Prog\Python\NFSR\storage')