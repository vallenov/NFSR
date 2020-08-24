import os
import time

def clear_way(dir):
    '''Clear directory'''
    for directory in os.listdir(dir):
        for file in os.listdir(dir+'\\'+directory):
            shutil.rmtree(dir+'\\'+directory+'\\'+file)

def scan(dir, to_dir, is_test):
    '''Scan receive directory'''
    tm = time.gmtime(time.time())
    for way in os.listdir(dir):
        fulldir = '\\'+way+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon)+'\\'+str(tm.tm_mday)+'\\'
        lstdir = os.listdir(dir+fulldir)
        if lstdir:
            print('In {} exist: '.format(dir+fulldir))
            print(lstdir)
            if not os.path.exists(to_dir+fulldir):
                print('Create new storage directory {}'.format(to_dir+fulldir))
                os.makedirs(to_dir+fulldir)
            for file in lstdir:
                if is_test:
                    print('Перемещаю файл {}'.format(file))
                else:
                    os.rename(dir+fulldir+file, to_dir+fulldir+file)
        time.sleep(1)

while True:
    scan(r'C:\Prog\Python\NFSR\receive',r'C:\Prog\Python\NFSR\storage',0)
