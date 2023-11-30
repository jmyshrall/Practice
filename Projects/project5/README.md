> COMP 424 Applied Computing: **Project 5**

### Purpose
- Learn and practice with text file processing
- Gain more practice with the histogram pattern: a special case of 
  accumulation pattern
- Use test-driven incremental development to document, test, design, 
    implement, and debug functions

### Examine the starter project
- Read the guidelines in this document. 
- Read the content of the  `file_processing.py` module. It has:
  - **function stubs**, consisting of 
    - function header: name and parameters of the function
    - function docstring, describing WHAT the function should do and its 
      parameters.
- Read the content of the `test_file_processing.py` module. It has function 
  stubs for testing functions that tests the functions in `file_processing.
  py` module. 
- Examine the context of all text files (extension `.txt`)
- Discuss and clarify in class
  - What problems the functions are supposed to solve
  - How the testing works and how to run the program.
  - Any other questions you have. 


### Document `file_processing.py` module
- Write your name as the program's developer
- Write the name of your collaborator(s)
- Write the date when you got started

### Develop the functions in `file_processing.py`
To completely develop each function, use the test-driven incremental 
development approach:
1. Understand and write test cases for the function. Implement **testing functions**
in `test_file_processing.py`. No design needed for test 
2. Write the design of the function
3. Implement the function. In `file_processing.py`.

#### 1. Understand and write test cases for the function
In the testing function definition in `test_file_processing.py`, the required test cases for each 
function. Use assignment statements to write the test case. 
- Define local variables and assign them concrete values that match the 
  function parameters
- Call the function with arguments that are the variable you just 
  defined. Assign the return value from the call to a `actual` variable. 
- Use another assignment statement to define variable `expected` and assign 
  to it the correct value you expect the function to return. 
- Write TWO print statements to print out `actual` and `expected`. When you 
  run the program, you'll compare whether they are the same.

In the **PyCharm Terminal**:
- Change directory with the `cd` bash command to be in the `project5` 
  directory 
- Run the program with the command `python test_file_processing.py`
  - Another way to run the module is to select **Current File** in the text 
    field next to a green arrow in the top menu bar. 
- If there are errors, find them and fix them.

In the **Problems** tab on the status menu bar:
- Check if there are code analysis and styling errors. 
- If there are errors, find them and fix them. 

#### Design the function
In the `DESIGN.md` file:
  - Outline the problem-solving steps
  - Use the outline to further describe the problem-solving steps in terms 
    of computations.

#### Implement the function
In the `file_processing.py` file
- Write the implementation based on the design.

In the **PyCharm Terminal**:
- Check that the current directory is `projectc5` with the bash command `pwd`
- Run the program with the command `file_processing.py`
- If there are errors, find them and fix them.

In the **Problems** tab:
- Check if there are code analysis and styling errors. 
- If there are errors, find them and fix them. 

### Evaluation
- Documentation: 10%
  - %5 for each module docstring
- Testing: 32%
  - 24%, %6 for each testing function
  - 8% for calling these functions in main
- Design: 32%, 8% for each function
- Implementation: 24%, 6% for each function
- Code analysis and styling: 10%

### Submission
- Go to https://github.com/orgs/2023-spring-comp-424 to find your 
  **project5-xxx** remote repo in GitHub.
- Use the `Add File --> Upload` and choose your local files for uploading:
  - `file_processing.py`
  - `test_file_processing.py`
  - ALL `.txt` files
  - `DESIGN.md
- Upload ONLY the files, do NOT upload the entire `project5` directory.
- Do NOT forget the text file.
