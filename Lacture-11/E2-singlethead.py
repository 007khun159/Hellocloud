import logging
import threading
import time 


def thread_function(name):
    logging.info('Thread %s: starting' ,name)
    time.sleep(2)
    logging.info("Thread %s: finsishing",name)

if __name__ == '__main__':
    format ="%(asctime)s: %(message)s"
    logging.basicConfig(format=format , level = logging.INFO, datefmt = "%H:%M:%S")


    logging.info("Main :        before creating thread")
    x = threading.Thread(target=thread_function , args=(1,),daemon=True)
    logging.info("Main  :       before running thred")
    x.start()
    logging.info("Main :        wait for the thread to finish")
    #ต้องประมวลผล join ให้เสร็จก่อนถึงจะ run ตามหลัง 
    x.join()
    logging.info("Main :        all done")



    