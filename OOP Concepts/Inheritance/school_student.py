class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, school, grade):
        super().__init__(name, age)
        self.school = school
        self.grade = grade

    def student_info(self):
        self.introduce()
        print(f"School: {self.school}, Grade: {self.grade}")


s1 = Student("Vatsal", 18, "The School of Science", "12th")
s1.student_info()
