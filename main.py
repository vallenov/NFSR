import os
import time
import logging

def scan(dir, to_dir, is_test):
    '''Scan receive directory'''
    tm = time.gmtime(time.time())
    for way in os.listdir(dir):
        fulldir = '\\'+way+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon)+'\\'+str(tm.tm_mday)+'\\'
        try:
            lstdir = os.listdir(dir+fulldir)
        except NotADirectoryError:
            logging.error("Exception occurred", exc_info=True)
        if len(lstdir) < 2:
            break
        if lstdir:
            print('In {} exist: '.format(dir+fulldir))
            print(lstdir)
            if not os.path.exists(to_dir+fulldir):
                print('Create new storage directory {}'.format(to_dir+fulldir))
                os.makedirs(to_dir+fulldir)
            for file in range(len(lstdir)-2):
                if is_test:
                    print('Move file {}'.format(lstdir[file]))
                else:
                    os.rename(dir+fulldir+lstdir[file], to_dir+fulldir+lstdir[file])
        #time.sleep(1)

while True:
    logging.basicConfig(filename='err.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%H:%M:%S %d-%b-%y')
    scan(r'C:\Prog\Python\NFSR\receive',r'C:\Prog\Python\NFSR\storage',0)
