> Project 5 Design Document

## line_count(filename)
```python
def line_count(filename):
    """
    Find and return the number of lines in the file named `filename`
    :param filename: string
    :return: non-negative integer
    """
```

### Problem Solving Steps
Count each new line in the file. 

### Computational Steps
- Open the file named `filename` using `with ... as ...`, `open()` 
  function call, and file object `f_in` 
- Use `f_in.readlines()` to get a list of lines of text in the file. Let's call it `lines_lst`
- Define accumulator `total_lines` of type integer, intialized with 0
- Use `for ... in ...`  to iterate through `lines_lst` with iterator `one_line`
  - At each iteration accumulate 1 into `total_lines`
- Return the accumulator `total_lines`


## Function header 2

### Problem Solving Steps

### Computational Steps

