> COMP 424 Applied Computing: **Homework 4**

### Purpose
- Practice and learn more about object-oriented design and programming
- Gain more practice with reading from and writing to text files
- Gain more practice with multiple Python modules and separating the 
  - development of the `Analysis` class and its instance methods in the 
    `analysis.py` module
  - demonstration of the methods in `main.py` mondul
- Use test-driven incremental development to document, test, design, 
    implement, and debug a class and its instance methods.

### Examine the starter project
- Read the guidelines in this document. 
- Read the content of the  `analysis.py` module. It has:
  - class `Analysis` stub: header and docstrings
  - instance methods stubs: headers and docstrings
- Read the content of the `main.py` module. It has:
  - function stubs for demonstrating the `Analysis` methods.
- Examine the content of the text files
  - Extension .csv stands for comma-separated values
- Check code analysis and style warnings and errors
  - Fix them, if you find fixable errors at this examination step.
- Run `pylint` and `pycodestyle` code analysis tools.
  - What errors do you get? Are the errors fixable?
- Run each module. 
  - What errors do you get? Why? Are the errors fixable
- Discuss and clarify in class any questions you have about this assignment. 

### Document both modules
- Write your name as the program's developer
- Write the date when you got started

### Develop the `Analysis` instance methods in `analysis.py` module
To develop each method, use the test-driven incremental development 
approach. Follow these 3 steps, in order, for ONE method at a time:
1. Understand and write the code in `main()` that tests and demonstrates 
   the functionality of the method with 3 different test cases, for each 
   of the CSV files 
2. Write the design of the method in `DESIGN.md`.
3. Implement the method in `analysis.py`.

#### 1. Understand and write test cases for the method
For each testing function in `main.py` write three test cases for 
the corresponding method. Use assignment statements to write the test case.   
- Define local variable and initalize it with the CSV file name
- Call the constructor with that local variable to create an object of type 
  `Analysis` and save it in `analysis_obj` variable
- Call the method on the `analysis_obj` object. 
  - For the `avg_hours()` amd `min_max_hours()` methods you need to define 
    and initalize an additional local variable BEFORE you make the call. 
    This is to create a value for the argument the call needs.  
- Assign the return value from the call to  `actual` variable. 
- Use another assignment statement to define variable `expected` and assign 
  to it the correct value you EXPECT the method to return. 
- Write TWO print statements to print out `actual` and `expected` variables.  
  When you run the program, you'll compare whether what gets printed is the 
  same.
- Note that the 4th testing function has a different implementation. Follow 
  guidelines provided in the function's docstring. 

In the **PyCharm Terminal** check the code analysis and styling warnings 
and errors. 
- Change directory with the `cd` bash command to be in the 
  `homework4` directory 
- Run the program with the command `python main.py`
  - Another way to run the module is to select **Current File** in the text 
    field next to a green arrow in the top menu bar. 
- If there are errors, find them and fix them.

In the **Problems** tab on the status menu bar:
- Check if there are code analysis and styling errors. 
- If there are errors, find them and fix them. 

Run `pylint` and `pycodestyhle` and fix any other code analysis and styling 
errors. 

#### 2. Design the method
In the `DESIGN.md` file:
  - Outline the problem-solving steps
  - Use the outline to further describe the **computational steps**. 

#### 3. Implement the method
In the `analysis.py` module
- Write the implementation based on the design.

Don't forget to check and fix all code analysis and styling errors using:
- PyCharm **Problems** tool
- `pytlin` and `pycodestyle` tools.

### Evaluation
- Documentation: 8%
  - %4 for each module docstring
- Demonstration: 36%
  - There are 4 testing function, each with 3 test cases corresponding to 
    the 3 CSV input files. 
  - Total of 12 mini-demos, 3% each mini-demo
- Design: 24%, 6% for each function
- Implementation: 20%, 5% for each function
- Code analysis and styling: 12%

### Submission
- Go to https://github.com/orgs/2023-spring-comp-424 to find your 
  **homework3-xxx** remote repo in GitHub.
- Use the `Add File --> Upload` and choose your local files for uploading:
  - `analysis.py`
  - `main.py`
  - `DESIGN.md`
  - All three CSV files
  - All three TXT files obtained from running `demo_report_avg()`
- Upload ONLY the files, do NOT upload the entire `practice_classes` directory.
