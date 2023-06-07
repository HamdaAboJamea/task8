
class Student :
    num_of_stds = 0

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.marks = []
        self.std_sum = 0



    def add_mark(self, mark):
        self.marks.append(mark)
        self.std_sum += mark

    def get_all_marks(self):
        for mark in self.marks:
            print(f"Mark = {mark}")

    def calc_average(self):
        if not self.marks:
            print("There are no marks for this student")
            return 0
        marks_sum = sum(self.marks)
        std_avg = self.std_sum / len(self.marks)
        return std_avg
std1 = Student("Hamda", 30, "Gaza")
print(std1.name)
print(std1.age)
print(std1.city)
std1.add_mark(90)
std1.add_mark(88)
std1.add_mark(70)
std1.add_mark(60)
std1.get_all_marks()
print(std1.calc_average())


std2 = Student("yasser", 22, "Absan")
print(std2.name)
print(std2.age)
print(std2.city)
std2.add_mark(60)
std2.add_mark(89)
std2.add_mark(71)
std2.add_mark(76)
std2.get_all_marks()
print(std2.calc_average())

std3 = Student("yasmine", 17, "Gaza")
print(std3.name)
print(std3.age)
print(std3.city)
std3.add_mark(100)
std3.add_mark(99)
std3.add_mark(98)
std3.add_mark(97)
std3.get_all_marks()
print(std3.calc_average())