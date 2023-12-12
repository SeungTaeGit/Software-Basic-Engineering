
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect
import tkinter as tk
from tkinter import messagebox
from Brainer import *
from NoBrainer import *
import random


def success() :
    R = random.randrange(1, 9)

    if (R == 1) :
        NoBrainer1()
    elif (R == 2) :
        NoBrainer2()
    elif (R == 3) :
        NoBrainer3()
    elif (R == 4) :
        NoBrainer4()
    elif (R == 5) :
        NoBrainer5()
    elif (R == 6) :
        NoBrainer6()
    elif (R == 7) :
        NoBrainer7()
    else :
        NoBrainer8()
    


def fail() :
    R2 = random.randrange(1, 7)

    if (R2 == 1) :
        Brainer1()
    elif (R2 == 2) :
        Brainer2()
    elif (R2 == 3) :
        Brainer3()
    elif (R2 == 4) :
        Brainer4()
    else :
        Brainer5()