class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.i = 0 
        self.score = 0
    
    def ask(self):
        q = self.questions[self.i]
        print(q['text'])
        print(q['options'])
        return q
    
    def check(self, ans):
        q = self.questions[self.i]
        if ans == q['correct']:
            self.score += 1
            print("Верно!")
        else:
            print(f"Неверно!")
    
    def next(self):
        self.i += 1
        return self.i < len(self.questions)


# База вопросов
questions = [
    {'id': 1, 'text': 'Столица России?', 
     'options': ['Москва', 'Питер', 'Новгород'], 'correct': 0},
    
    {'id': 2, 'text': 'Сколько ног у паука?', 
     'options': ['6', '8', '10'], 'correct': 1},
    
    {'id': 3, 'text': 'Какого цвета небо?', 
     'options': ['Зелёное', 'Красное', 'Синее'], 'correct': 2},
    
    {'id': 4, 'text': 'Зимний месяц?', 
     'options': ['Май', 'Июнь', 'Декабрь'], 'correct': 2},
    
    {'id': 5, 'text': '2 + 2 * 2 = ?', 
     'options': ['4', '6', '8'], 'correct': 1}
]


quiz = Quiz(questions)

while quiz.i < len(questions):
    q = quiz.ask()
    ans = int(input())
    quiz.check(ans)
    quiz.next()


print(f"ИГРА ОКОНЧЕНА!")
print(f"Результат: {quiz.score}/{len(questions)}")