def phishing_quiz():
    print("\n🔐 Welcome to Phishing Awareness Training!\n")
    score = 0

    questions = [
        {
            "q": "1. You receive an email claiming you won a lottery. It asks for your bank details. What should you do?",
            "options": ["A. Reply with details", "B. Ignore/Delete email", "C. Click the link"],
            "answer": "B"
        },
        {
            "q": "2. A website URL looks like 'paypa1.com' instead of 'paypal.com'. Is this safe?",
            "options": ["A. Yes", "B. No"],
            "answer": "B"
        },
        {
            "q": "3. Which is a common sign of phishing?",
            "options": ["A. Urgent tone in message", "B. Grammatical errors", "C. Suspicious links", "D. All of the above"],
            "answer": "D"
        }
    ]

    for q in questions:
        print("\n" + q["q"])
        for opt in q["options"]:
            print(opt)
        ans = input("Your answer: ").strip().upper()
        if ans == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong! The correct answer is:", q["answer"])

    print(f"\n🏆 Training Completed! Your score: {score}/{len(questions)}")
    if score == len(questions):
        print("🎉 Excellent! You can recognize phishing attempts.")
    else:
        print("⚠ Review phishing awareness material to improve.")

if _name_ == "_main_":
    phishing_quiz()