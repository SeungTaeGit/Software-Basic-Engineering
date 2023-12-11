import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect
import tkinter as tk
from tkinter import messagebox


# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)

# 점수 반환 값
score = 0


# 첫 번째 쉬운 문제
def NoBrainer1():

    def check_answer():
        user_input = entry.get()
        correct_answers = {"OS", "Operating System"}
        global score

        if user_input in correct_answers:
            messagebox.showinfo("정답 확인", "정답입니다!")
            score = int(1)
            root.destroy()
        else:
            messagebox.showerror("정답 확인", "틀렸습니다. 다시 시도하세요.")
            score = int(0)
            root.destroy()
    
    # tkinter 창 생성
    root = tk.Tk()
    root.title('Operating System')
    root.geometry('750x150')

    q = tk.Label(root, text="다음의 설명을 보고 알맞는 답을 제출하시오.")
    d = tk.Label(root, text="'이것'은 사용자가 컴퓨터의 하드웨어를 쉽게 사용할 수 있도록 인터페이스를 제공해주는 소프트웨어다.")

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


# 두 번째 쉬운 문제
def NoBrainer2():

    def check_answer():
        user_input = entry.get()
        correct_answers = {"Data Link Layer", "Data Link"} 
        global score

        if user_input in correct_answers:
            messagebox.showinfo("정답 확인", "정답입니다!")
            score = int(1)
            root.destroy()
        else:
            messagebox.showerror("정답 확인", "틀렸습니다. 다시 시도하세요.")
            score = int(0)
            root.destroy()

    # tkinter 창 생성
    root = tk.Tk()
    root.title('Network')
    root.geometry('750x150')

    q = tk.Label(root, text="다음의 설명을 보고 알맞는 답을 제출하시오.")
    d = tk.Label(root, text="'이 계층'은 OSI 7 계층의 한 부분으로 `링크의 설정`, `유지`, `종료 담당 및 노드 간의 회선제어`, `흐름제어`, `오류제어` 등의 역할을 담당한다.")

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


# 세 번째 쉬운 문제
def NoBrainer3():

    def check_answer():
        user_input = entry.get()
        correct_answers = {"->"} 
        global score
        
        if user_input in correct_answers:
            messagebox.showinfo("정답 확인", "정답입니다!")
            score = int(1)
            root.destroy()
        else:
            messagebox.showerror("정답 확인", "틀렸습니다. 다시 시도하세요.")
            score = int(0)
            root.destroy()

    # tkinter 창 생성
    root = tk.Tk()
    root.title('Programming Language')
    root.geometry('750x150')

    q = tk.Label(root, text="다음의 설명을 보고 알맞는 답을 제출하시오.")
    d = tk.Label(root, text="'이 연산자'는 c언어의 구조체 포인터 안의 변수에, 즉 멤버 변수에 쉽게 접근할 수 있도록 해준다.")

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


# 네 번째 쉬운 문제
def NoBrainer4():

    def check_answer():
        selected_answer = var.get()
        global score

        if selected_answer == 1:
            messagebox.showinfo("정답 확인", "정답입니다! 👍")
            score = int(1)
            root.destroy()
        else:
            messagebox.showerror("정답 확인", "틀렸습니다. 다시 시도하세요.")
            score = int(0)
            root.destroy()

    root = tk.Tk()
    root.title("Programming Language")

    # 화면 크기 설정
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{int(screen_width * 0.6)}x{int(screen_height * 0.6)}")

    # 문제, 보기, 버튼 가운데 정렬을 위한 프레임 생성
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True)

    question = "[문제] 올바른 자기 참조 구조체 정의를 고르시오."
    answers = [
        "①\n    struct list {\n        int num;\n        struct list *next;\n    };",
        "\n",  # 추가된 줄
        "②\n    struct list {\n        int num;\n        struct list next;\n    };"
    ]

    question_label = tk.Label(main_frame, text=question, font=("Times New Roman", 16))  # 폰트 변경
    question_label.pack(pady=(20, 30))

    var = tk.IntVar()

    answers_frame = tk.Frame(main_frame)
    answers_frame.pack()

    for i, answer in enumerate(answers):
        if i == 1:  # 1번과 2번 보기 사이의 추가적인 줄
            spacer_label = tk.Label(answers_frame, text=answer, font=("Times New Roman", 14))  # 폰트 변경
            spacer_label.pack(pady=5)
        else:
            radio_button = tk.Radiobutton(answers_frame, text=answer, variable=var, value=i+1, font=("Times New Roman", 14), justify='left')  # 폰트 변경
            radio_button.pack(anchor='w', padx=10, pady=5)

    submit_button = tk.Button(main_frame, text="확인", command=check_answer, font=("Times New Roman", 14))  # 폰트 변경
    submit_button.pack(pady=20)

    result_label = tk.Label(main_frame, text="", font=("Times New Roman", 16))  # 폰트 변경
    result_label.pack()

    root.mainloop()


# 다섯 번째 쉬운 문제
def NoBrainer5():
    def 문제생성():
        question_label.config(text="변수를 선언할 때 사용하는 기호는? ")

    def 정답_확인():
        사용자_답 = entry.get()
        정답 = "="
        global score


        if 사용자_답 == 정답:
            messagebox.showinfo("결과", "정답입니다!")
            score = int(1)
            root.destroy()
        else:
            messagebox.showerror("결과", "틀렸습니다!")
            score = int(0)
            root.destroy()

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
    root.geometry("400x200")

    # 문제 표시 레이블
    question_label = tk.Label(root, text="")
    question_label.pack()

    # "문제 생성" 버튼
    create_button = tk.Button(root, text="문제 생성", command=문제생성_버튼_클릭)
    create_button.pack()

    root.mainloop()


def back2():
    return score