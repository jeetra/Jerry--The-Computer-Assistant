from playsound import playsound
import random
import os
from multiprocessing import Process


def sound():
    os.system("python startup.py")


def video():
    os.system("python vibrant_circle.py")

'''def sound1():
    ls=['Formula1.mp3','MI.mp3','T&M.mp3']
    playsound(random.choice(ls))'''

if __name__ == '__main__':
    p1 = Process(target = sound)
    p1.start()
    p2 = Process(target = video)
    p2.start()
    #p3=Process(target = sound1)
    #p3.start()


#os.system('python jerry.py')
