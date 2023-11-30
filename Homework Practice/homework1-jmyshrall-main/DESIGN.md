> Project 2 Design Document

## count_odd() Function Design
- **Input**: List integers, `num_list`
- **Output**: Sum of the squares of the integers in the list. 


### Problem Solving Steps
*Write here the problem-solving steps*
- find a list of integers contained within `lst`
- check if each number in `lst` is odd by seeing if they have a remainder when divided by 2
- add amount of odd numbers to `count`
- print total odd numbers as `Number of odd integers in the list:`

### Computational Steps
*Describe here the computational steps*

- create the variable `count`, class int and initialize with 0 
- use `for` to loop a check for every `num` within `lst`
- At each iteration of checking
  - divide `num` by 2 and determine if result has a remainder using `% 2 != 0`
  - if there is a remainder add `num` to count total using `+=`
- return `count`
- print `count`