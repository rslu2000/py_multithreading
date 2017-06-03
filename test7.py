#coding:utf-8
import multiprocessing as mp
import time
import hashlib
import random


#正常程序 在產生 新的process 會從 原本 process
#完整複製同一份 記憶體 , 所以新的process 最一開始
#會和主程序 記憶體內容完全相同,但隨著時間過去 而不同
#所以變數之間 process不能共用

#例子
#rand 在 新的 process 得到隨機職
#rand2 在 主程序 得到隨機職

#理論上rand1 會和其他process 不同
#而rand2 則相同


rand1 = 0
rand2 = random.randint(0,1000)

def job(a):
    global rand1,rand2
    rand1=random.randint(0,1000)
    s=a
    for i in range(2500000):
        s=hashlib.sha256(s).hexdigest()
    print ('hash:'+s)
    print ('rand1:'+str(rand1))
    print ('rand2:'+str(rand2))
        

def main():
    start = time.time()
    p1 = mp.Process(target=job,args=('string_1',))
    p2 = mp.Process(target=job,args=('string_2',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print end - start, 'seconds'

if __name__=='__main__':
    main()
