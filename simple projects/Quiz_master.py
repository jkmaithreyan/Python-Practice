questions =[
    {"question": "Capital of India", "answer": "new delhi"},
    {"question": "2 + 2 = ?", "answer": "4"},
    {"question": "color of sky", "answer": "blue"}
]

score_count = 0

for q in questions:
    user_input = input(f"{q['question']} --> Enter your answer: ")
    user_input = user_input.strip().lower()
    if user_input == q["answer"]:
        score_count = score_count + 1
    
print(f"Total score --> {score_count}/3")
print(f"percentage --> {score_count/3 * 100}")
if score_count == 3:
    print("A Grade")
elif score_count == 2:
    print("B Grade")
elif score_count == 1:
    print("C Grade")
else:
    print("Fail")


