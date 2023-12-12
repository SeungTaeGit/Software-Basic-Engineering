import pygame
import sys
import os
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# 첫 번째 어려운 문제
def Des():

    root = tk.Tk()
    root.title("Description")
    root.geometry("1200x600")


    description = (
        "최단 경로 게임에 오신 것을 환영합니다!\n\n"
        "게임 목표 : 집에서 학교까지 가는 최단 경로를 찾는 것입니다.\n"
        "게임을 시작하면 맵 상에 여러 경로들이 나타날 것이며 \n"
        "문제를 풀며 최적의 경로를 찾아야 합니다.\n\n"
        "게임 시작 버튼을 눌러 학교로 빨리 가보세요!"
    )

    def start_game():
        messagebox.showinfo("게임 시작", "게임을 시작합니다!\n\n최단 경로를 찾아 집에서 학교까지 안전하게 이동하세요.")

    button_start = tk.Button(root, text="게임 시작", command=start_game, border=5, font=("Helvetica", 20))
    button_start.place(x=870, y=200)

    def show_rules():
        messagebox.showinfo("게임 규칙 설명", description)

    button_rules = tk.Button(root, text="게임 규칙", command=show_rules, border=5, font=("Helvetica", 20))
    button_rules.place(x=870, y=300)

    def exit_game():
        messagebox.showinfo("게임 종료", "게임을 종료합니다!")
        root.destroy()

    button_exit = tk.Button(root, text="종료하기", command=exit_game, border=5, font=("Helvetica", 20))
    button_exit.place(x=870, y=400)

    root.mainloop()
