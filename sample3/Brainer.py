import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect
import tkinter as tk
from tkinter import messagebox
import random

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
    root.geometry('600x300')

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
        code_lines ="""
        a=0
        while True:
            a+= 1
            print(a)
            if a == 10:
                break
        """
        
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


# 네 번째 어려운 문제
def Brainer4():
    def check_password():
        password = entry_guess.get()
        if password == "2580":
            doorlock_label.config(text="띠로링~ 문이 열렸습니다!", fg="green")
            entry_guess.delete(0, tk.END)
            next_step_button.pack()
            root.destroy()
        else:
            doorlock_label.config(text="삐빅. 비밀번호가 틀렸습니다.", fg="red")
            entry_guess.delete(0, tk.END)
            root.destroy()
            over()

    def button_click(number):
        current = entry_guess.get() + str(number)
        entry_guess.delete(0, tk.END)
        entry_guess.insert(tk.END, current)

    def show_hint():
        root.withdraw()  # 1번 코드 창 숨기기
        hint_window = tk.Toplevel(root)
        hint_window.title("도어락 비밀번호 힌트")

        password_digits = [2, 5, 8, 0]
        current_index = 0
        attempt_count = 0  # 시도 횟수 초기화

        result_label = tk.Label(hint_window, text="1번째 숫자를 입력하세요.", fg="blue")
        result_label.pack()

        entry_guess = tk.Entry(hint_window, width=20)
        entry_guess.pack()

        buttons_frame = tk.Frame(hint_window)
        buttons_frame.pack()

        def create_button(number):
            return tk.Button(buttons_frame, text=str(number), padx=20, pady=10, command=lambda: button_click(number))

        for i in range(1, 10):
            button = create_button(i)
            button.grid(row=(i - 1) // 3, column=(i - 1) % 3)

        button_zero = tk.Button(buttons_frame, text='0', padx=20, pady=10, command=lambda: button_click(0))
        button_zero.grid(row=3, column=1)

        remaining_attempts_label = tk.Label(hint_window, text="남은 횟수: 10", fg="black")
        remaining_attempts_label.pack()

        def button_click(number):
            current = entry_guess.get()
            entry_guess.delete(0, tk.END)
            entry_guess.insert(tk.END, str(current) + str(number))
            
        def check_guess():
            nonlocal current_index, attempt_count

            user_input = entry_guess.get()

            if len(user_input) != 1 or not user_input.isdigit():
                result_label.config(text="한 자리 숫자를 입력하세요.", fg="orange")
                return

            user_digit = int(user_input)

            attempt_count += 1
            remaining_attempts = 10 - attempt_count
            remaining_attempts_label.config(text=f"남은 횟수: {remaining_attempts}")

            if remaining_attempts <= 0:
                result_label.config(text="실패! 횟수 초과", fg="red")
                check_button.config(text="뒤로가기")
            elif user_digit == password_digits[current_index]:
                current_index += 1
                entry_guess.delete(0, tk.END)
                if current_index < 4:
                    result_label.config(text=f"{current_index}번째 숫자를 맞췄습니다! 다음 숫자를 입력하세요.", fg="blue")
                else:
                    result_label.config(text=f"축하합니다! 비밀번호는 2580 입니다.", fg="green")
                    entry_guess.config(state='disabled')
                    check_button.config(text="도어락 열기", command=Brainer5)  # 여기서 도어락 열기 버튼을 첫 번째 창으로 돌아가게 설정
            elif user_digit < password_digits[current_index]:
                result_label.config(text="업! 더 큰 숫자를 입력하세요.", fg="orangered")
            else:
                result_label.config(text="다운! 더 작은 숫자를 입력하세요.", fg="orangered")
            entry_guess.delete(0, tk.END)

        check_button = tk.Button(hint_window, text="확인", padx=13, pady=10, command=check_guess)
        check_button.pack()

        def open_door():
            hint_window.destroy()  # 2번 코드 창 닫기
            root.deiconify()  # 1번 코드 창 다시 보이기

    root = tk.Tk()
    root.title("도어락 열기")

    doorlock_window = tk.Frame(root)
    doorlock_window.pack()

    doorlock_label = tk.Label(doorlock_window, text="도어락", font=("Arial", 16, "bold"))
    doorlock_label.pack()

    buttons_frame = tk.Frame(doorlock_window)
    buttons_frame.pack()

    doorlock_label.config(text="도어락", font=("Arial", 16, "bold"))

    entry_guess = tk.Entry(doorlock_window, width=0, show='*')
    example_text = tk.Label(doorlock_window, text="ex) 1234*", font=("Arial", 10))
    example_text.pack()

    hint_button = tk.Button(doorlock_window, text="힌트", command=show_hint)
    hint_button.pack()

    buttons = []
    button_text = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#']
    for i in range(12):
        button = tk.Button(buttons_frame, text=button_text[i], width=4, height=2, command=lambda num=button_text[i]: button_click(num))
        button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
        buttons.append(button)

    for btn in buttons:
        if btn.cget("text") == "*":
            btn.config(command=check_password)

    next_step_button = tk.Button(doorlock_window, text="다음 단계")
    next_step_button.pack_forget()

    root.mainloop()


# 다섯 번째 어려운 문제
def Brainer5():

    # tkinter 창 생성
    root = tk.Tk()
    root.title('Square')
    root.geometry('500x300')

    def check_answer():
        user_input = entry.get()
        correct_answers = {"O(n^2)"} 

        if user_input in correct_answers:
            messagebox.showinfo("정답 확인", "정답입니다!")
            root.destroy()
        else:
            messagebox.showerror("정답 확인", "GAME OVER!")
            root.destroy()
            over()

    code = """
    def print_each_n_times(li):
    for n in li:
        for m in li:
            print(n,m)
    """

    q = tk.Label(root, text="다음 코드에 맞는 빅O(Big-O) 표기법을 작성하시오.")
    q.pack(pady=5)

    text_widget = tk.Text(root, wrap="none", width=40, height=10)
    text_widget.pack(pady=10)
    text_widget.insert("1.0", code)
    text_widget.configure(state="disabled")

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