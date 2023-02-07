from __init__ import *
import threading
import time

def t1():
    sign=True
    index=1
    while sign:
        print(index)
        index+=1
        time.sleep(3)
        if index>3:
            sign=False

if __name__ == "__main__":
    T1 = threading.Thread(target=t1, name="T1")
    T1.start()
    print('1111111')