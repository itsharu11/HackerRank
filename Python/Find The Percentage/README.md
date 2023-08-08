

## Description

This code takes input for `n` number of students and their marks in 3 subjects. The marks are stored in a dictionary with the student names as keys. The program then takes input for a `query_name` and calculates the average marks for that student. The average marks are printed with two decimal places.

## Usage

1. Run the program.
2. Enter the number of students (`n`).
3. Enter the name and marks of each student separated by a space. Repeat this step for all `n` students.
4. Enter the name of the student for which you want to calculate the average marks.
5. The program will output the average marks of the specified student.

## Example

```
Input:
3
John 78 89 91
Alice 82 76 88
Bob 90 94 87
Alice

Output:
82.00
```

## Note

The program assumes that the input for the marks is separated by spaces and that there are no additional spaces before or after the names and marks.

## CODE EXPLAINATION

```
if __name__ == '__main__':
```
This line checks whether the current script is being run as the main program or not. If it is, then the code below will be executed. This is a common way to ensure that code only runs when the script is run directly and not when it is imported as a module.

```
n = int(input())
```
This line prompts the user to enter an integer value and stores it in the variable `n`. This value is used to determine how many students' marks will be entered.

```
student_marks = {}
```
This line creates an empty dictionary called `student_marks` which will be used to store the names and marks of the students.

```
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
```
This is a for loop that runs `n` times, which was the value inputted earlier. In each iteration of the loop, it prompts the user to enter a student's name and their corresponding marks separated by spaces. The `split()` method splits the input string into a list of strings using spaces as the delimiter. The `*line` notation is used to collect all the remaining values from the split into a list called `line`. The `map()` method applies the `float()` function to each value in the `line` list and returns a map object, which is then converted to a list using the `list()` function. The resulting list of floats is assigned to the variable `scores`. Finally, the student's name and their list of scores are added as a key-value pair to the `student_marks` dictionary.

```
query_name = input()
result = sum(student_marks[query_name])/3
print("{:.2f}".format(result))
```
This code prompts the user to enter the name of the student whose average marks they wish to calculate. The `sum()` function is used to sum up all the marks of the student whose name was inputted and then divided by the number of marks, which is 3 since we are assuming each student has 3 marks. The resulting value is assigned to the variable `result`. Finally, the `print()` function displays the result with two decimal places using the `"{:.2f}".format()` notation.