import threading
import logging
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
        my_thread = threading.Thread(target=doubler, name=thread_names[i],args=(i,logger))
        my_thread.start()