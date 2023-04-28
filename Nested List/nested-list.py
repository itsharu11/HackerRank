
n = int(input())
student = []
grades = []
lst = []
for x in range (n):
    name = str(input())
    grade = float(input())
    student.append([name,grade])
    grades.append(grade)
    
sl = sorted(set(grades))[1]

for student in sorted(student):
    if student[1] == sl:
        print(student[0])
        
    

