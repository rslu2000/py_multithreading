import threading as td
import time
import hashlib


def job(a):
    s=a
    for i in range(2500000):
        s=hashlib.sha256(s).hexdigest()
    print (s)
        

def main():
    start = time.time()
    t1 = td.Thread(target=job,args=('string_1',))
    t2 = td.Thread(target=job,args=('string_2',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print end - start, 'seconds'

if __name__=='__main__':
    main()
