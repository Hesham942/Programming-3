import threading
from time import sleep, ctime
def loop0():
    print('start loop 0 at time:', ctime())
    sleep(4)
    print('done loop 0 at time:', ctime())
def loop1():
    print('start loop 1 at time:', ctime())
    sleep(2)
    print('done loop 1 at time:', ctime())
if __name__ == '__main__':
    print('starting program at time:', ctime())
    threading.Thread(target=loop0).start()
    threading.Thread(target=loop1).start()
    sleep(6)
    print('done program at time:', ctime())


## using locks ##

import threading
from time import sleep, ctime
loops = [4,2]
def loop(nloop, nsec, lock):
    print( 'start loop ',nloop,' at time: ', ctime())
    sleep(nsec)
    print ('done loop ',nloop,' at time: ', ctime())
    lock.release()
if __name__=='__main__':
    print ('starting program at time: ', ctime())
    locks = []
    nloops = range(len(loops))
    for l in nloops:
        lock = threading.Lock()
        lock.acquire()
        locks.append(lock)
    for l in nloops:
        threading.Thread(target=loop, args=(l, loops[l], locks[l])).start()
    for l in nloops:
        while locks[l].locked(): 
            pass 
    print ('done program at time: ', ctime() )