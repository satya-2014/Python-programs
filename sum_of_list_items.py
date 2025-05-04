student_marks=[10,20,30,40,31]
print("Sum of student marks => ",sum(student_marks))
print(f"Sum of student marks => {sum(student_marks)}")

#Another way
sum=0
for marks in student_marks:
    sum+=marks
print(sum)

