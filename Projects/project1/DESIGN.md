## Initial Problem
- **Input**: Get the number of years from the user.
- **Output**: Print out the number of minutes corresponding to the given 
  number of 
  years. 

### Problem Solving Steps
*Forget about using programming to automate the problem solving 
process. Concentrate on devising a plan to solve the problem. What are the 
intermediate, logical steps for getting the output from the intput?* 

	 - First assign an input value for years that will be used
        in computing
    - Then assign years to the integer 'year' so there is a     
    value to use
    - Then assign values using arithmatic operators starting 
    by taking years
    - Take years and assign as days when multiplied by 365. 
    - Take days and assign as hours when multiplied by 24
    - Take hours and assign as minutes when multiplied by 60
    - Then print the value for 'minutes' giving the correct output

### Computational Steps
*Translate your plan and logical steps into computational steps*
	
	Input from user in terms of years using input command
    convert input from int to str using ""
    Assign years as variable, 'year'
	Multiply years by 365, assign as days
	Multiply 365 by 24, assign as hours
	multiply 24 by 60, assign as minutes
	get output in minutes

## Quesiton 1
- **Input**: Get the number of years from the user.
- **Output**: Print out the number of seconds corresponding to the number of 
  years. 

### Problem Solving Steps
*Reuse what's appropriate from the previous problem.
    
    - First assign an input value for years that will be used
        in computing
    - Then assign years to the integer 'year' so there is a     
    value to use
    - Then assign values using arithmatic operators starting 
    by taking years
    - Take years and assign as days when multiplied by 365. 
    - Take days and assign as hours when multiplied by 24
    - Take hours and assign as minutes when multiplied by 60
    - Take minutes and assign as seconds when multiplied by 60
    - Then print the value for'seconds' giving the correct output

### Comoputational Steps
	- Input from user in terms of years using input()
    - Assign years as integer, 'year' using int()
	- Multiply years by 365, assign as days using =
	- Multiply 365 by 24, assign as hours using = 
    - Multiply 24 by 60, assign as minutes using = 
	- Multiply 60 by 60, assign as seconds using = 
    - Get output in seconds using print()

## Question 2
- **Input**: Get the number of seconds from the user.
- **Output**: Print out the years corresponding to the number of seconds. 
- **Assumptions**: We assume that the year has 365 days (we ignore leap years)

*Write the computational steps to answer this question. Reuse what's 
  appropriate from the design of previous problems.*
    
    - Use input() command to get amount of 'seconds' 'from user
    - Convert seconds from str to int using int()
    - Assign seconds as the variable, 'seconds'
    - Divide variable by 60, assign as minutes
    - Divide 60 by 60, assign as hours using =
    - Divide 60 by 24, assign as days using =
    - Divide 24 by 365, assign as years using = 
    - Get output in years and print using print()

## Question 3
- **Input**: Get the number of seconds from the user.
- **Output**: Print out the number of years, number of months, number of days, 
  and number of minutes corresponding to the given number of seconds. 
- **Assumptions**: 
  - Ignore leap years. 
  - Consider that all months have 30 days.
- **Hint**: Use integer division and modulo operator to avoid decimal 
    numbers. For example, dviding 65 seconds by 60 should give you 1 minutes 
    and 6 seconds, not 1.08333333. 

### Problem Solving Steps
        The code should start with an input allowing a user to 
        assign values. Similar to the other parts arthimatic is used
        The input would be divided by 60 using // in order to 
        get only and integer with no decimals and minutes. 
        Similar divisions would occur to get hours, days, and years
        months are now included and come before years in the block
        Now the months and days need to utilize the years in their 
        calculation. This is done using the % command which returns
        the remainder of dividing two numbers which lets us calculate
        the correct output. Lastly the values will be printed
        in str in order.
        
### Computational Steps
        - Give the user an input statement that asks for seconds 
        using input()
        - Convert seconds from str to int using int()
        - Take input and divide by 60 using // to cancel remainder
        - Divide minutes by 60 using // gets hours
        - Divide hours by 24 using // gets days
        - Divide days by 30 using // gets months
        - Divide months by 12 using // gets years
        - Make months assigned to the variable months returning 
        the division remainder using % 12 
        - Assign days to days returning the division remainder 
        using % 30
        - Print the str 'years' as years print()
        - Print the str 'months' as months print()
        - Print the str 'days' as days print()
        - Print the str 'minutes' as minutes print()
        - Output will appear on four different text lines for each output
        
        
