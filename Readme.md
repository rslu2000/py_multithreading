1. test1.py using "from thread import *" and one statement like "start_new_thread(doubler, (arg i,))".

2. test2.py using "import threading" and the statements like "my_thread = threading.Thread(target=doubler, args=(i,))" and "my_thread.start()". We also output the message to the debug log file.

3. test3.py using "import threading" and inherit the parent class "threading.Thread" then using the statements as the followings:
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
4. test4.py using multiprocessing to do 2 sub-processes call for sha256 calulation<br/>
5. test5.py using regular function call to do 2 times sha256 calulation<br/>
6. You can comapre the execution time between test4.py and test5.py, then you will find the efficency in multiprocessing.<br/>
7. test6.py using multithreading to do 2 sub-threading call for sha256 calculation, you can find that multithreading cannot save time in cpu-consuming task.<br/>
<img src="https://github.com/rslu2000/py_multithreading/blob/master/profile.png" /img><br/>

</body></html>