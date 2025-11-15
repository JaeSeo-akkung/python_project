import random

def play_rps():
    choices = ["가위", "바위", "보"]
    print("🎮 가위바위보 게임 시작!")
    print("선택지:", choices)

    while True:
        user = input("👉 가위, 바위, 보 중 하나를 입력하세요 (종료하려면 q): ")
        if user == "q":
            print("게임을 종료합니다. 👋")
            break
        if user not in choices:
            print("❌ 잘못된 입력입니다. 다시 시도하세요.\n")
            continue

        computer = random.choice(choices)
        print(f"🖥️ 컴퓨터의 선택: {computer}")

        if user == computer:
            print("🤝 비겼습니다!\n")
        elif (user == "가위" and computer == "보") or \
             (user == "바위" and computer == "가위") or \
             (user == "보" and computer == "바위"):
            print("🎉 당신이 이겼습니다!\n")
        else:
            print("😢 당신이 졌습니다...\n")

if __name__ == "__main__":
    play_rps()