from juprog import CircleProgress
from time import sleep

def test():
    for _ in CircleProgress(range(10)):
        sleep(0.2)
