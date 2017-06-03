1. test1.py using "import thread" and "start_new_thread(doubler, (arg i,))".

2. test2.py using "import threading" and the statements like "my_thread = threading.Thread(target=doubler, args=(i,))" and "my_thread.start()". We also output the message to the debug log file.

3. test3.py using "import threading" and inherit the parent class "threading.Tread" then using the statements as the followings:
<html><body><p>
class MyThread(threading.Thread):<br/>
     def __init__(self, arg1, arg2):<br/>
            threading.Thread.__init__(self)<br/>
            self.number = arg1<br/>
            self.logger= arg2<br/>
      def run (self)<br/>
      doubler(self.number, self.logger)<br/>
 
thread = MyThread (number, logger)<br/>
thread.start() <br/></p>
</body></html>