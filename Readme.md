test1.py using "import thread" and "start_new_thread(doubler, (arg i,))".

test.py using "import threading" and the statements like "my_thread = threading.Thread(target=doubler, args=(i,))" and "my_thread.start()".

test3.py using "import threading" and inherit the parent class "threading.Tread" then using the following statements as the followings:

class MyThread(threading.Thread):
     def __init__(self, arg1, arg2):
            threading.Thread.__init__(self)
            self.number = arg1
            self.logger= arg2
      def run (self)
      doubler(self.number, self.logger)
# starting creat the threads
thread = MyThread (number, logger)
thread.start()