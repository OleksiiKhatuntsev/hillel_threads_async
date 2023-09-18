from threading import Thread
from time import sleep


def make_tea(tea_name, range_value):
    for tea in range(range_value):
        print(f"using INNER thread {tea} {tea_name}")
        sleep(0.5)


my_thread = Thread(target=make_tea, args=("Lipton", ), kwargs={"range_value": 5})
my_thread.start()
my_thread.join()

for tea in range(5):
    print(f"using MAIN thread {tea} Greenfield")
    sleep(0.5)