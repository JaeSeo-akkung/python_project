import sys

# 퀴즈 데이터 (문제, 선택지, 정답 인덱스)
quiz = [
    {
        "question": "세계에서 가장 큰 사막은 무엇일까요?",
        "options": ["고비 사막", "사하라 사막", "아라비아 사막", "남극 사막"],
        "answer": 3
    },
    {
        "question": "피타고라스의 정리에 따르면 직각삼각형의 빗변 제곱은 무엇과 같을까요?",
        "options": ["두 직각변의 제곱 합", "두 변의 합", "두 직각변의 제곱 차", "두 변의 곱"],
        "answer": 0
    },
    {
        "question": "지구에서 가장 깊은 바다는 어디일까요?",
        "options": ["대서양", "태평양", "인도양", "북극해"],
        "answer": 1
    },
    {
        "question": "로마 숫자에서 'X'는 어떤 숫자를 의미할까요?",
        "options": ["10", "5", "100", "50"],
        "answer": 0
    },
    {
        "question": "에디슨이 발명한 것으로 가장 유명한 것은 무엇일까요?",
        "options": ["전구", "라디오", "자동차", "전화기"],
        "answer": 0
    }
]

def run_quiz():
    print("🎮 퀴즈 게임을 시작합니다!\n")
    score = 0

    for i, q in enumerate(quiz, 1):
        print(f"Q{i}. {q['question']}")
        for idx, opt in enumerate(q["options"], 1):
            print(f"   {idx}. {opt}")
        
        try:
            choice = int(input("👉 정답 번호를 입력하세요: ")) - 1
        except ValueError:
            print("❌ 숫자를 입력해야 합니다!\n")
            continue

        if choice == q["answer"]:
            print("✅ 정답!\n")
            score += 1
        else:
            print(f"❌ 오답! 정답은 {q['options'][q['answer']]} 입니다.\n")

    print(f"🎉 게임 종료! 총 점수: {score}/{len(quiz)}")

if __name__ == "__main__":
    run_quiz()