import json

def run_quiz():
    # Load questions from a JSON file
    with open('questions.json', 'r') as file:
        questions = json.load(file)

    score = 0

    # Loop through the questions
    for q in questions:
        print(q["question"])
        for idx, option in enumerate(q["options"], 1):
            print(f"{idx}. {option}")

        user_choice = int(input("Enter the number of your answer: "))
        user_answer = q["options"][user_choice - 1]

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"You scored {score} out of {len(questions)}.")

# Run the quiz
run_quiz()
