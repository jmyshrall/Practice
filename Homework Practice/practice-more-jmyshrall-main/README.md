> COMP 424 Applied Computing: **More Practice with Classes**

### Purpose
- Learn and practice with classes and file processing

### Examine the starter project
- Read the guidelines in this document. 
- Read the content of the  `olympics.py` module. It has:
  - **function stubs**, consisting of 
    - function header: name and parameters of the function
    - function docstring, describing WHAT the function should do and its 
      parameters.
- Read the content of the `test_olympics.py` module. It has function 
  stubs for testing functions that tests the functions in `olympics.
  py` module. 
- Examine the context of all text files (extension `.txt`)
- Discuss and clarify in class
  - What problems the functions are supposed to solve
  - How the testing works and how to run the program.
  - Any other questions you have. 


### Document `olympics.py` and `test_olympics.py` module
- Write your name as the program's developer
- Write the name of your collaborator(s)
- Write the date when you got started

### Build a class from the functions in `olympics.py`
- Defind the class `Olympics`
- Discuss what instance variables objects of the class should have
- Convert the functions into methods

### Develop the methods in the `Olympics` class in  `olympics.py` module
To completely develop each method, use the test-driven incremental 
development approach:
1. Understand and write test cases for the method. No design 
   is required to implement a testing function.
2. Write the design of the method in `DESIGN.md`.
3. Implement the method in `olympics.py`.

#### 1. Understand and write test cases for the method
In the testing function definition (in `test_olympics.py`), write the 
required test cases for each method. Use assignment statements to write the 
test case.   
- Define local variables and assign them concrete values that match the 
  method parameter(s)
- Call the method with arguments that are the variable you just 
  defined. Assign the return value from the call to  `actual` variable. 
- Use another assignment statement to define variable `expected` and assign 
  to it the correct value you EXPECT the method to return. 
- Write TWO print statements to print out `actual` and `expected` variables.  
  When you run the program, you'll compare whether what gets printed is the 
  same.

In the **PyCharm Terminal**:
- Change directory with the `cd` bash command to be in the 
  `practice-classes_more` directory 
- Run the program with the command `python test_olypincs.py`
  - Another way to run the module is to select **Current File** in the text 
    field next to a green arrow in the top menu bar. 
- If there are errors, find them and fix them.

In the **Problems** tab on the status menu bar:
- Check if there are code analysis and styling errors. 
- If there are errors, find them and fix them. 

#### 2. Design the method
In the `DESIGN.md` file:
  - Outline the problem-solving steps
  - Use the outline to further describe the **computational steps**. 

#### 3. Implement the method
In the `olympics.py` file
- Write the implementation based on the design.

In the **PyCharm Terminal**:
- Check that the current directory is `practice-classes_more` directory 
  with the bash command `pwd` 
- Run the program with the command `python olympics.py`
- If there are errors, find them and fix them.

In the **Problems** tab:
- Check if there are code analysis and styling errors. 
- If there are errors, find them and fix them. 

### Self-Evaluation
- Documentation: 10%
  - %5 for each module docstring
- Testing: 28%
  - 20%, %5 for each testing function
  - 8% for calling these functions in `main()` in `test_olympics.py`
- Design: 32%, 8% for each function
- Implementation: 20%, 5% for each function in `file_processing.py`
- Code analysis and styling: 10%

### Submission
- Go to https://github.com/orgs/2023-spring-comp-424 to find your 
  **project5-xxx** remote repo in GitHub.
- Use the `Add File --> Upload` and choose your local files for uploading:
  - `olympics.py`
  - `test_olympics.py`
  - ALL `.txt` files
  - `DESIGN.md`
- Upload ONLY the files, do NOT upload the entire `practice-more-xxx` 
  directory.
- Do NOT forget the text file.
