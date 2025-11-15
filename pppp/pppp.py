import tkinter as tk
import random

def generate_numbers():
    # 1~7 사이의 랜덤 숫자 3개 생성
    numbers = [random.randint(1, 7) for _ in range(3)]
    
    # 숫자를 레이블에 표시
    for i, num in enumerate(numbers):
        number_labels[i].config(text=str(num))

    # 숫자가 모두 같으면 축하 메시지 표시
    if len(set(numbers)) == 1:
        result_label.config(text="축하합니다!", fg="red", font=("Arial", 24, "bold"))
    else:
        result_label.config(text="")

# 메인 윈도우 생성
root = tk.Tk()
root.title("숫자 게임")

# 숫자를 표시할 레이블 생성
number_labels = [tk.Label(root, text="0", font=("Arial", 36)) for _ in range(3)]
for label in number_labels:
    label.pack(side=tk.LEFT, padx=10)

# 결과 메시지 레이블
result_label = tk.Label(root, text="", font=("Arial", 18))
result_label.pack(pady=20)

# 시작 버튼 생성
start_button = tk.Button(root, text="시작", command=generate_numbers, font=("Arial", 14))
start_button.pack(pady=10)

# GUI 실행
root.mainloop()