import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect
import tkinter as tk
from tkinter import messagebox



# 첫 번째 어려운 문제
def Des():

    # tkinter 창 생성
    root = tk.Tk()
    root.title('Des')
    root.geometry('700x400')

    
    d = tk.Label(root, text="설명")

    d.pack(pady=5)

    # tkinter 창 실행
    root.mainloop()