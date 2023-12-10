import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect
import tkinter as tk
from tkinter import messagebox


# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)

# 점수 반환 값
score = 0


def fail() :
    # 새 창 설정
    new_window_width, new_window_height = 800, 600
    new_window = pygame.display.set_mode((new_window_width, new_window_height))
    pygame.display.set_caption("새로운 창")

    new_window.fill(white)  # 새 창을 흰색으로 채우기
    pygame.display.flip()  # 화면 업데이트
    pygame.time.delay(1000)  # 1초 동안 대기
    new_window.fill(black)  # 새 창을 검은색으로 채우기
    pygame.display.flip()  # 화면 업데이트


def Start():

    # tkinter 창 생성
    root = tk.Tk()
    root.title('Operating System')
    root.geometry('700x400')

    def check_answer():
        user_input = entry.get()
        correct_answers = {"5"} 
        global score

        if user_input in correct_answers:
            messagebox.showinfo("정답 확인", "정답입니다!")
            score = int(1)
            root.destroy()
        else:
            messagebox.showerror("정답 확인", "틀렸습니다. 다시 시도하세요.")
            score = int(0)
            root.destroy()

    q = tk.Label(root, text="다음 `스택`의 연산이 행해진 후의 결과를 작성하시오. (단, 입출력의 연산은 스택의 연산이 모두 끝난 후 한번에 시행된다.)")
    d = tk.Label(root, text="PUSH 5\nPUSH 8\nPOP\nPUSH *\nPUSH -\nPUSH 12\nPUSH +\nPOP\nPOP\nPOP\nPUSH 3\nPOP\nPOP\nPOP")

    q.pack(pady=5)
    d.pack(pady=5)

    # 엔트리 위젯
    entry = tk.Entry(root, width=20)
    entry.pack(pady=5)

    # 버튼 위젯
    button = tk.Button(root, text="정답 확인", command=check_answer)
    button.pack(pady=5)

    # tkinter 창 실행
    root.mainloop()


def back():
    return score
