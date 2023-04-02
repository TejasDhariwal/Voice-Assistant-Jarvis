
from threading import Thread
import time

def add():
    a = 0
    print("addition started.")
    for i in range(10):
        a += i
    print(f"Addition completed \n answer :- {a}")

def minus():
    b = 0
    print("subtraction started.")
    for i in range(10):
        b -= i
    print(f"subtraction completed \n answer :- {b}")

def product():
    c = 5
    print("multiplication started.")
    for i in range(1, 11):
        print(f"{c} X {i} = {c*i}")

    print("multiplication completed.")



threadList = []

threadList.append(Thread(target=add))
threadList.append(Thread(target=minus))
threadList.append(Thread(target=product))

for task in threadList:
    task.start()

for task in threadList:
    task.join()
