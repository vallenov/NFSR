import time
import random
import os
import shutil

def clear_way():
    for i in range(1,6):
        for file in os.listdir(r'C:\Prog\Python\NFSR\receive\way'+str(i)):
            shutil.rmtree(r'C:\Prog\Python\NFSR\receive\way'+str(i)+'\\'+file)


i = 0
clear_way()
while i < 100:
    way = random.randint(1,5)
    filename = time.time()
    tm = time.gmtime(time.time())
    if not os.path.exists(os.getcwd()+'\\'+'way'+str(way)+'\\'+str(tm.tm_year)):
        print(os.getcwd()+'\\'+'way'+str(way)+'\\'+str(tm.tm_year))
        os.mkdir(os.getcwd()+'\\'+'way'+str(way)+'\\'+str(tm.tm_year))
    if not os.path.exists(os.getcwd()+'\\'+'way'+str(way)+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon)):
        os.mkdir(os.getcwd()+'\\'+'way'+str(way)+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon))
    if not os.path.exists(os.getcwd()+'\\'+'way'+str(way)+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon)+'\\'+str(tm.tm_mday)):
        os.mkdir(os.getcwd()+'\\'+'way'+str(way)+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon)+'\\'+str(tm.tm_mday))

    f = open(os.getcwd()+'\\'+'way'+str(way)+'\\'+str(tm.tm_year)+'\\'+str(tm.tm_mon)+'\\'+str(tm.tm_mday)+'\\'+'file'+str(filename), 'w')
    print('file'+str(filename)+' create')
    for inf in range(1000000):
        f.write('test ')
    print('file'+str(filename)+' fill')
    f.close
    i += 1
    time.sleep(random.randint(2,5))