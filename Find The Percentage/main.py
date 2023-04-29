Student_Dictionary = {}

n = int(input())


for i in range(n):
    name = input()
    
    # for x in range(3):
    marks = input()
    Student_Dictionary[name] = marks
    # print(Student_Dictionary) 
    
query_name = input()

if query_name in Student_Dictionary():
    res = sum(Student_Dictionary[query_name])
    
print(res)