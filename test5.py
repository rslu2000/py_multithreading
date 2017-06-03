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
    job('string_1')
    job('string_2')
    end = time.time()
    print end - start, 'seconds'

if __name__=='__main__':
    main()
