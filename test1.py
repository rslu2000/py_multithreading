
from thread import *
import threading

def doubler(number):
    print(threading.currentThread().getName()+'\n')
    result=number *2
    print (result)
    
if __name__=='__main__':
    for i in range(5):
        my_thread = threading.Thread(target=doubler, args=(i,))
        my_thread.start()
# another multithreading call
    start_new_thread(doubler,(20,))
