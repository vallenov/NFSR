import time
import random
import os
import shutil

def genfiles(dir):
    i = 0
    lst = os.listdir(dir)
    while i < 100:
        way = random.randint(0,len(lst)-1)
        tm = time.gmtime(time.time())
        if not os.path.exists(dir+'\\'+lst[way]+'\\'+str(tm.tm_year)):
            os.mkdir(dir+'\\'+lst[way]+'\\'+str(tm.tm_year))
        if not os.path.exists(dir+'\\'+lst[way]+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon)):
            os.mkdir(dir+'\\'+lst[way]+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon))
        if not os.path.exists(dir+'\\'+lst[way]+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon)+'\\'+str(tm.tm_mday)):
            os.mkdir(dir+'\\'+lst[way]+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon)+'\\'+str(tm.tm_mday))
        filename = 'file'+str(tm.tm_year)+'-'+str(tm.tm_mon)+'-'+str(tm.tm_mday)+'_'+str(tm.tm_hour)+str(tm.tm_min)+str(tm.tm_sec)
        f = open(dir+'\\'+lst[way]+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon)+'\\'+str(tm.tm_mday)+'\\'+str(filename), 'w')
        print(str(filename)+' create')
        for inf in range(1000000):
            f.write('test ')
        print(str(filename)+' fill')
        f.close
        i += 1
        #time.sleep(random.randint(2,5))

genfiles(r'C:\Prog\Python\NFSR\receive')