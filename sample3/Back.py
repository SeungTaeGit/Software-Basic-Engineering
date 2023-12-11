
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect
import tkinter as tk
from tkinter import messagebox
from Brainer import *
from NoBrainer import *
import random


def success() :
    R = random.randrange(1, 6)

    if (R == 1) :
        NoBrainer1()
    elif (R == 2) :
        NoBrainer2()
    elif (R == 3) :
        NoBrainer3()
    elif (R == 4) :
        NoBrainer4()
    else :
        NoBrainer5()
    


def fail() :
    R2 = random.randrange(1, 4)

    if (R2 == 1) :
        Brainer1()
    elif (R2 == 2) :
        Brainer2()
    else :
        Brainer3()