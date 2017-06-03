1. test1.py using "import thread" and "start_new_thread(doubler, (arg i,))".

2. test2.py using "import threading" and the statements like "my_thread = threading.Thread(target=doubler, args=(i,))" and "my_thread.start()". We also output the message to the debug log file.

3. test3.py using "import threading" and inherit the parent class "threading.Tread" then using the following statements as the followings:
<p>
class MyThread(threading.Thread):
     def __init__(self, arg1, arg2):
            threading.Thread.__init__(self)
            self.number = arg1
            self.logger= arg2
      def run (self)
      doubler(self.number, self.logger)
 
thread = MyThread (number, logger)
thread.start() </p>