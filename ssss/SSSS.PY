import random

def number_guessing_game():
    print("🎮 숫자 맞추기 게임 시작!")
    print("1부터 100 사이의 숫자를 맞춰보세요.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("👉 숫자를 입력하세요: "))
        except ValueError:
            print("❌ 숫자만 입력 가능합니다.\n")
            continue

        attempts += 1

        if guess < secret_number:
            print("🔼 더 큰 숫자입니다.\n")
        elif guess > secret_number:
            print("🔽 더 작은 숫자입니다.\n")
        else:
            print(f"🎉 정답! {attempts}번 만에 맞추셨습니다.")
            break

if __name__ == "__main__":
    number_guessing_game()