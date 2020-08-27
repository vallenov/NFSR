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
            logger.exception("Exception occurred")
        if len(lstdir) < 2:
            break
        if lstdir:
            logger.warning('In {} exist: '.format(dir+fulldir))
            logger.warning(lstdir)
            if not os.path.exists(to_dir+fulldir):
                logger.warning('Create new storage directory {}'.format(to_dir+fulldir))
                try:
                    os.makedirs(to_dir+fulldir)
                except NotADirectoryError:
                    logger.exception("Exception occurred")
            for file in range(len(lstdir)-2):
                if is_test:
                    logger.warning('Move file {}'.format(lstdir[file]))
                else:
                    try:
                        os.rename(dir+fulldir+lstdir[file], to_dir+fulldir+lstdir[file])
                    except FileExistsError:
                        logger.exception("Exception occurred")
        #time.sleep(1)

logger = logging.getLogger(__name__)
console_log = logging.StreamHandler()
file_log = logging.FileHandler('error.log')

console_log.setLevel(logging.WARNING)
file_log.setLevel(logging.ERROR)

console_log_format = logging.Formatter('%(asctime)s - %(message)s', datefmt='%H:%M:%S %d-%b-%y')
file_log_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

console_log.setFormatter(console_log_format)
file_log.setFormatter(file_log_format)

logger.addHandler(console_log)
logger.addHandler(file_log)

while True:
    scan(r'C:\Prog\Python\NFSR\receive',r'C:\Prog\Python\NFSR\storage',0)
