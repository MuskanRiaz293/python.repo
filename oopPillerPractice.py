# Define a class named Student
class Student:
    # Constructor to set up data for each student
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Method 1
    def study(self):
        print(f"{self.name} is studying.")

    # Method 2
    def take_exam(self):
        print(f"{self.name} is taking an exam.")


# Create student objects
student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 22, "B")

# Call methods
student1.study()      # Output: Alice is studying.
student2.take_exam()  # Output: Bob is taking an exam.
