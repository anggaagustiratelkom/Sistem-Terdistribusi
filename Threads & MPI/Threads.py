import threading
import time
import random
arr = []

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print "Starting " + self.name
      # Get lock to synchronize threads
      threadLock.acquire()
      print_time(self.name, self.counter, 1)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName, delay, counter):
   
   while counter:
      time.sleep(delay)
      x = random.randint(18,37)
      print (threadName, time.ctime(time.time()), x)
      arr.append(x)
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Suhu Subang", 1)
thread2 = myThread(2, "Suhu Kediri", 2)
thread3 = myThread(3, "Suhu Padang", 3)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

# Wait for all threads to complete
for t in threads:
    t.join()
print''
print "Suhu Rata-Rata: ", sum(arr)/len(arr)
