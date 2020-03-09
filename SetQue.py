import queue
import time
import multiprocessing
import threading

from twittwer_api import Get_twitter
from textToImage import setAllImg
from imgToVideo import imgToVideo


def worker(i):
  while True:
    item = q.get()

    qSize = q.qsize()
    if item is None:
      print("Thread %s has finished all the works. XD" % i)
      break

    print("Thread " +str(i)+ " process on 1 task"  + " from current " + str(qSize) + " tasks......")
    #do_work(item)
    # after get all images, then get videos
    setAllImg(item)
    imgToVideo(item)

    print("Thread %s has completed the TASK <%s>. @_@" % (i, item))
    
    q.task_done()



# test 
hashtag = ['James', 'Kobe', 'James Harden', 'Curry', 'Wade', 'Trump']

# Build threads
num_of_threads = 4
threads = []

# build queue
q = queue.Queue()


# how to wait for enqueued tasks to be completed
# reference: https://docs.python.org/2/library/queue.html  
for i in range(1, num_of_threads+1):
  t = threading.Thread(target=worker, args=(i,))
  threads.append(t)
  t.start()


# put items in queue
for item in hashtag:
  q.put(item)


# Blocks until all items in the queue have been gotten and processed.
q.join()

print("\n---------All works done---------\n")

# put threads in queue
for i in range(num_of_threads):
  q.put(None)
# join thread in threads list
for j in threads:
  t.join()

#print the information of all the thread
print("\nThreads Information:")
for t in threads:
  print(t)