class Student:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Location: {self.location}"

# 학생 개체 생성
student1 = Student("최유정", 23, "남양주")
student2 = Student("최유정", 23, "남양주")
student3 = Student("최유정", 23, "남양주")

# 학생 정보 출력
print(student1)
print(student2)
print(student3)

print(student1.name)
print(student1. age)
print(student1.location)

class Classroom:
    def __init__(self, *students_info): # * 계속 가져다 붙일 때 쓰는거
        self.students = []
        for info in students_info:
            self.add_student(*info)

    def add_student(self, name, age, location):
        student = Student(name, age, location)
        self.students.append(student)

    def list_students(self):
        for student in self.students:
            print(student)

# 여러 학생 정보를 넣어 Classroom 인스턴스를 생성합니다.
classroom = Classroom(('이상욱', 47, '서울'), ('홍길동', 16, '부산'), ('김철수', 15, '대구'))
# 학생들의 목록을 출력합니다.
classroom.list_students()

# 두 번째 Classroom 인스턴스를 생성합니다.
classroom2 = Classroom(('김유민', 23, '영암'), ('홍길동', 16, '부산'), ('김철수', 15, '대구'))
# 학생들의 목록을 출력합니다.
classroom2.list_students()

# 학생들 정보를 한꺼번에 가져온다면 아래처럼 함수로도 만들 수 있긴 함.
def student_info(name, age, location):
    return "Name: {0}, Age: {1}, Location: {2}".format(name, age, location)

student1 = student_info("최유정", 23, "남양주")
student2 = student_info("최유정", 23, "남양주")
student3 = student_info("최유정", 23, "남양주")

print(student1)
print(student2)
print(student3)



