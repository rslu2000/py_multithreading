import threading
import logging

class MyThread(threading.Thread):
    def __init__(self, arg1, arg2):
        threading.Thread.__init__(self)
        self.number = arg1
        self.logger= arg2
    def run (self):
        logger.debug('Calling doubler')
        doubler(self.number, self.logger)

def get_logger():
    logger=logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("threading.log")
    fmt='%(asctime)s-%(threadName)s-%(levelname)s-%(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

def doubler(number,logger):

    logger.debug('Doubler function executing')
    result=number *2
    logger.debug('Double function ended with:{}'.format(result))

    
if __name__=='__main__':
    logger=get_logger()
    thread_names=['Mike','George','Wanda','Nina','Tracy']

    for i in range(5):
        thread=MyThread(i,logger)
        thread.setName(thread_names[i])
        thread.start()