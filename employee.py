import time
from time import sleep
from threading import Lock, RLock, Semaphore, Thread


class Employee:
    def __init__(self):
        self._salary = 0
        self.age = 20
        self._lock = Lock()
        self._rlock = RLock()
        self._semaphore = Semaphore(1)

    def increase_salary(self):
        # temp_age = self.age
        # temp_age += 1
        # sleep(0.5)
        # self.age = temp_age
        # print("get data from db")
        # print("or download file")
        # with self._lock:
        self._rlock.acquire()
        self._rlock.acquire()
        temp_value = self._salary
        temp_value += 100
        sleep(0.5)
        self._salary = temp_value
        self._rlock.release()
        self._rlock.release()

emp = Employee()

thread_1 = Thread(target=emp.increase_salary)
thread_2 = Thread(target=emp.increase_salary)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(emp._salary)