#for loop that uses zip() functionality
#declare two lists 
print("Lets play a fun game of questions and answers")
#questions 
question_input = input("questions: ")
questions = question_input.split()
#answers
answer_input = input("answers: ")
answers = answer_input.split()
#if check if answers and questions are the same length
if len(questions) != len(answers):
#check which one is shorter and by what
    if len(questions) < len(answers):
        new_question_input = input(f"Kindly enter {len(answers) - len(questions)} more questions: ")
        new_questions = new_question_input.split()
        if len(new_questions) != len(answers) - len(questions):
            new_questions_input = input(f"Kindly enter {(len(answers) - len(questions)) - len(new_questions)} more questions: ")
            new_questions.append(new_questions_input.split())
        #append the new input to the list
        questions.append(new_questions)
    elif len(answers) < len(questions):
        new_answers_input = input(f"Kindly enter {len(questions) - len(answers)} more answers: ")
        new_answers = new_answers_input.split()
        if len(new_answers) != len(questions) - len(answers):
            new_answers_input = input(f"Kindly enter {(len(questions) - len(answers)) - len(new_answers)} more answers: ")
            new_answers.append(new_answers_input.split())
        #append the new input to the list
        answers.append(new_answers)
#use the for loop and zip()
for q, a in zip(questions, answers):
    print(f"""What is your {q}?
It is {a}""")
