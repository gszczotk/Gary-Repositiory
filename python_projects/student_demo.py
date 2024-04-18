from student import Student

student1 = Student("Gary", "Szczotka", 123456)

print(student1)
print()
student1.greeting()
print()

print(f"Energy level is {student1.get_energy_level()}")
student1.take_exam()
print(f"Energy level after the exam is {student1.get_energy_level()}")