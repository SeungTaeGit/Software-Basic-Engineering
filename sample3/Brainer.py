import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect
import tkinter as tk
from tkinter import messagebox

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)

# 점수 반환 값
score = 0

def over():
    pygame.quit()
    sys.exit()

# 첫 번째 어려운 문제
def Brainer1():

    # tkinter 창 생성
    root = tk.Tk()
    root.title('Data Structure')
    root.geometry('700x400')

    def check_answer():
        user_input = entry.get()
        correct_answers = {"5"} 

        if user_input in correct_answers:
            messagebox.showinfo("정답 확인", "정답입니다!")
            root.destroy()
        else:
            messagebox.showerror("정답 확인", "GAME OVER!")
            root.destroy()
            over()

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


# 두 번째 어려운 문제
def Brainer2():

    # tkinter 창 생성
    root = tk.Tk()
    root.title('Programming Language')
    root.geometry('700x400')

    def check_answer():
        user_input = entry.get()
        correct_answers = {"AB"} 

        if user_input in correct_answers:
            messagebox.showinfo("정답 확인", "정답입니다!")
            root.destroy()
        else:
            messagebox.showerror("정답 확인", "GAME OVER!")
            root.destroy()
            over()

    c_code = """
    #include <stdio.h>

    void main() {
        int a = 10;

        switch(++a) {
            case 11: printf("A");
            case 12: printf("B");
        }
    }
    """

    q = tk.Label(root, text="다음 c 언어로 이루어진 코드의 예상 출력을 작성하시오.")
    q.pack(pady=5)

    text_widget = tk.Text(root, wrap="none", width=40, height=10)
    text_widget.pack(pady=10)
    text_widget.insert("1.0", c_code)
    text_widget.configure(state="disabled")

    # 엔트리 위젯
    entry = tk.Entry(root, width=20)
    entry.pack(pady=5)

    # 버튼 위젯
    button = tk.Button(root, text="정답 확인", command=check_answer)
    button.pack(pady=5)

    # tkinter 창 실행
    root.mainloop()


# 세 번째 어려운 문제
def Brainer3():

    def 문제생성():
        code_lines ='''
            a=0
            while True:
                a+= 1
                print(a)
                if a == 10:
                   break
        '''
        
        code = code_lines
        question_label.config(text=code)

    def 정답_확인():
        사용자_답 = entry.get()
        정답 = "12345678910"
        if 사용자_답 == 정답:
            messagebox.showinfo("정답 확인", "정답입니다!")
            root.destroy()
        else:
            messagebox.showerror("정답 확인", "GAME OVER!")
            root.destroy()
            over()


    def 정답입력_창_표시():
        # 정답 입력 라벨
        answer_label = tk.Label(root, text="정답을 입력하세요:")
        answer_label.pack()

        # 정답 입력 필드
        global entry
        entry = tk.Entry(root)
        entry.pack()

        # 정답 확인 버튼
        confirm_button = tk.Button(root, text="정답 확인", command=정답_확인)
        confirm_button.pack()

    def 문제생성_버튼_클릭():
        문제생성()
        정답입력_창_표시()

    # Tkinter 창 생성
    root = tk.Tk()
    root.title("문제 풀기")

    # 창 크기 설정
    root.geometry("600x300")

    # 문제 표시 레이블
    question_label = tk.Label(root, text="")
    question_label.pack()

    # "문제 생성" 버튼
    create_button = tk.Button(root, text="문제 생성", command=문제생성_버튼_클릭)
    create_button.pack()

    root.mainloop()


def back():
    return score