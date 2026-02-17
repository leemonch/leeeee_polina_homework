class Diary:
    def __init__(self):
        self.__grades = {}
    def add_grade(self, subject, grade):
        if isinstance(subject, str) and subject != "" and isinstance(grade, int) and 2 <= grade <= 5:
            if subject not in self.__grades:
                self.__grades[subject] = [] 
            self.__grades[subject].append(grade)
    def get_average(self, subject):
        if subject in self.__grades and len(self.__grades[subject]) > 0:
            grades_list = self.__grades[subject]
            return sum(grades_list)/len(grades_list)
        return 0.0 
    def get_all_average(self):
        all_grades = []
        for grades_list in self.__grades.values(): #возвращает все значения без ключей
            all_grades.extend(grades_list) #добавляет все эл-ты в конец списка
        if len(all_grades) == 0:
            return 0.0
        return sum(all_grades) / len(all_grades)
    def get_bad_subjects(self):
        bad_subjects = []
        for subject in self.__grades:
            avg = self.get_average(subject)
            if avg < 3.5:
                bad_subjects.append(subject)
        return bad_subjects
    def reset_diary(self):
        self.__grades.clear()

my_diary = Diary()

my_diary.add_grade("Биология", 5)
my_diary.add_grade("Биология", 5)
my_diary.add_grade("Биология", 5)
my_diary.add_grade("Химия", 2)
my_diary.add_grade("Химия", 3)

print(my_diary.get_average("Биология"))   
print(my_diary.get_average("Химия"))     
print(my_diary.get_all_average())         
print(my_diary.get_bad_subjects())       

my_diary.reset_diary()
