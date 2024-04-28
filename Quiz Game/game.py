questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. London", "B. Paris", "C. Rome", "D. Madrid"],
        "correct_answer": "B. Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Mars", "B. Jupiter", "C. Venus", "D. Saturn"],
        "correct_answer": "A. Mars"
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["A. H2O", "B. CO2", "C. O2", "D. NaCl"],
        "correct_answer": "A"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "choices": ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"],
        "correct_answer": "A"
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Gorilla"],
        "correct_answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["A. Au", "B. Ag", "C. Fe", "D. Cu"],
        "correct_answer": "A"
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "choices": ["A. Tomatoes", "B. Avocado", "C. Onions", "D. Peppers"],
        "correct_answer": "B"
    },
    {
        "question": "What is the tallest mountain in the world?",
        "choices": ["A. Mount Everest", "B. K2", "C. Kilimanjaro", "D. Mount Fuji"],
        "correct_answer": "A"
    },
    {
        "question": "Which gas do plants use to photosynthesize?",
        "choices": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "correct_answer": "C"
    },
    {
        "question": "What is the largest ocean in the world?",
        "choices": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
        "correct_answer": "C"
    }
]

score = 0

for i, question in enumerate(questions):
    print(f"Question {i+1}: {question['question']}")
    for choice in question['choices']:
        print(choice)
    answer = input("Enter your answer (A, B, C, or D): ")
    if answer.upper() == question['correct_answer'][0]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer is {question['correct_answer']}")
    print(f"Your score: {score}/{i+1}\n")

print(f"Total score: {score}/{len(questions)}")
if score == len(questions):
    print("You are a genius!")