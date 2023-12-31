class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        text = current_question.text
        answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {text}. (True/False): \n")

        self.check_answer(user_answer, answer)

    def still_has_question(self):

        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 1
        else:
            self.score += 0

        print(f"Your current score is {self.score}/{self.question_number}")






