Structure:

cs4300 /
| - - homework1 /
| | - - src /
| | | - - task1 . py
| | | - - task2 . py
| | | - - task3 . py
| | | - - task4 . py
| | | - - task5 . py
| | | - - task6 . py
| | \ - - task7 . py
| | - - tests /
| | | - - test_task1 . py
| | | - - test_task2 . py
| | | - - test_task3 . py
| | | - - test_task4 . py
| | | - - test_task5 . py
| | | - - test_task6 . py
| | \ - - test_task7 . py
| | - - task6_read_me . txt
| \ - - README.md
\

Task 1:
task1.py
Function: hello_world()
Description: Returns string "Hello, World!"
Purpose: Shows a simple python function and testing

test_task1.py
Function tested: hello_world
Assertion: The functiom needs to return "Hello, World!"
Instructions:
cd cs4300
pytest tests/test_task1.py

Task 2:
task2.py
Functions:
- add_int(x, y) # Returns the sum of two integers
- mult_float(x, y) # Returns the product of two floats
- check_str(name) # Returns a greeting with name provided
- check_bool(num) # Returns True if even or False if odd
Purpose: Demonstrate basic operations with different data types

test_task2.py
Functions tested: 
- add_int(x, y)
- mult_float(x, y)
- check_str(name) 
- check_bool(num)
Assertion:
4 + 5 == 9
4.5 * 5.5 == 24.75
"Rayne" == "Hi, Rayne! How are you?"
4 is True
5 is False 
Instructions:
cd cs4300
pytest tests/test_task2.py

Task 3:
task3.py
Functions:
- add_int(x, y) # Returns the sum of two integers
- mult_float(x, y) # Returns the product of two floats
- check_str(name) # Returns a greeting with name provided
- check_bool(num) # Returns True if even or False if odd
Purpose: Demonstrate basic operations with different data types

test_task3.py
Functions tested: 
- check_num(num) # Returns whether a number is `"positive"`, `"negative"`, `"zero"`, or `"not a number"`
-  print_prime_nums() # Returns the first 10 prime numbers
-  get_sum() # Returns the sum of numbers from 0 to 100
Assertion:
print(task3.check_num(3)) # positive
print(task3.check_num(-3)) # negative
print(task3.check_num(0)) # zero
print(task3.print_prime_nums()) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(task3.get_sum()) # 5050
Instructions:
cd cs4300
pytest tests/test_task3.py
