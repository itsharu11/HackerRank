Python script that defines a function called `split_and_join`. 

1. `def split_and_join(line):`: This line defines a function named `split_and_join` that takes one parameter, `line`, which is expected to be a string.

2. `line = line.split(" ")`: This line splits the input `line` into a list of words using spaces as separators. The result is stored back in the `line` variable.

3. `line = "-".join(line)`: This line joins the list of words in `line` back together into a single string, using hyphens (`-`) as separators.

4. `result = line`: The modified string in the `line` variable is assigned to the `result` variable.

5. `return result`: The function returns the modified string.

6. The `if __name__ == '__main__':` block is a common Python construct that ensures the code inside it is only executed when the script is run directly (not when imported as a module).

7. `line = input()`: This line takes input from the user. The user is expected to enter a string.

8. `result = split_and_join(line)`: The `split_and_join` function is called with the user's input as an argument, and the result is stored in the `result` variable.

9. `print(result)`: Finally, the modified string is printed to the console.

In summary, when you run this script, it will take a string input from the user, split it into words using spaces, join the words back together using hyphens, and then print the modified string.