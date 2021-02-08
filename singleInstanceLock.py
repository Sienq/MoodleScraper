import os
import time


def waitAndLock(lock_file_name):

    while True:

        if os.path.exists(lock_file_name) == False:
            break

        time.sleep(1)
    
    lock_file = open(lock_file_name, "w")
    lock_file.close()


def removeLock(lock_file_name):
    os.remove(lock_file_name)