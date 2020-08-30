import os
import time
import logging

def benchmark(func):
    def cover(dir, to_dir, is_test):
        start = time.time()
        func(dir, to_dir, is_test)
        finish = time.time() - start
        logger.warning('Benchmark is {:.4} sec'.format(finish))
    return cover

@benchmark
def scan(dir, to_dir, is_test):
    '''Scan receive directory'''
    tm = time.gmtime(time.time())
    cnt_move = 0
    for way in os.listdir(dir):
        fulldir = '\\'+way+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon)+'\\'+str(tm.tm_mday)+'\\'
        try:
            lstdir = os.listdir(dir+fulldir)
        except FileNotFoundError:
            break
        if lstdir:
            logger.warning('In {} exist: {}'.format(dir+fulldir, lstdir))
            if not os.path.exists(to_dir+fulldir):
                logger.warning('Create new storage directory {}'.format(to_dir+fulldir))
                os.makedirs(to_dir+fulldir)
            for file in range(len(lstdir)):
                if is_test:
                    logger.warning('Move file {}'.format(lstdir[file]))
                else:
                    try:
                        os.rename(dir+fulldir+lstdir[file], to_dir+fulldir+lstdir[file])
                    except IOError:
                        logger.warning(f'File {lstdir[file]} is busy')
                        time.sleep(1)
                    else:
                        logger.warning('Move file {} from {} to {}'.format(lstdir[file], dir+fulldir, to_dir+fulldir))
                        cnt_move += 1
                logger.warning(f'Finish scan in {dir+fulldir}')
    logger.warning(f'Scan final. {cnt_move} files was moved')

logger = logging.getLogger(__name__)
console_log = logging.FileHandler('move.log')
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
    scan(r'C:\Prog\Python\NFSR\receive',r'C:\Prog\Python\NFSR\storage', 0)
