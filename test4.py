import multiprocessing as mp
import time
import hashlib


def job(a):
    s=a
    for i in range(2500000):
        s=hashlib.sha256(s).hexdigest()
    print (s)
        

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
