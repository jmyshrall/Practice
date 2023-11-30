> Project 2 Design Document

##E sum_of_square() Function Desgin
- **Input**: List integers, `num_list`
- **Output**: Sum of the squares of the integers in the list. 


### Problem Solving Steps
- Find list of integers contained within `number_list`
- Square each number contained in `number_list`
- Add all squares 
- Print final sum as `result`

### Computational Steps
- Create `result` variable, of type int, initialized with 0 
- Use for loop to go through `number_list` with loop variable `num`
- At each iteration
  - Square `num` and add it to `result`
- Return `result`
- Print `result`