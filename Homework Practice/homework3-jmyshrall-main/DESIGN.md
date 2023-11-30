> Homework 3 Design Document

## def read_data(filename):
``python
def read_data(filename):
    """
    Read the text file named filename to report the hours recorded for each
    student in the file. Each file line has strings separated by commas:
    - 1st string is the name of the student
    - the following strings represent study hours
    :param filename: str, name of the file
    :return: dictionary
        keys are strings, representing student names
        values are list of integers, corresponding to the study hours
    Example: If filename is `data_2.csv`,
        the function returns: {'joe':[10,8,5,10], 'sue':[7,9,10]}
    """
``
### Problem Solving Steps
- Look at text and see what names work what hours
- Separate each name into a group and assign hours to each name group
- Write out each name with respective hours worked

### Computational Steps
- Begin an accumulation using a blank dictionary using `{}` assigned as `data`
- Open the file named `filename` using `with ... as ...` and `open()` function call,
and file object `f`
  - iterate through `f` using loop variable `line`
    - split the text in the file using `.split(',')` to separate text assign as `fields`
    - assign the `names` as their position in `fields` by indexing at `0`
    - covert values `h` indexed after `1` to type `int` and assign as `hours`
      - loop through fields after pos `1` using loop variable `h`
    - store `names` and `hours` as key value pairs using `[]` assign as `hours`
- return data

## def sum_hours(filename):
````
def sum_hours(filename):
    """
    Find the total number of study hours for each student.
    :param filename: dictionary
        keys are strings, representing student names
        values are list of integers, corresponding to the study hours
    :return: dictionary, keys are student names, values are hour averages.
    Example: if `student_hours_d` is {'joe':[10,8,5,10], 'sue':[7,9,10]}
        the function returns {'joe':33, 'sue':26}
    """
````
### Problem Solving Steps
- Look through file and see what names go to what hours
- take the names and their respective hours and sum the hours
- take name and put it with the total sum of their hours along with other names and their hours

### Computational Steps
- Begin an accumulation using an empty dictionary `{}`, assigned as `total_hours`
- Open the file named `filename` using the `with ... as ...` statement and the `open()` function call,
and file object `f`
  - Iterate through the lines of the `file` using a `for` loop with loop variable `line`
    - Split each line into a list of fields using the `.split(',')` method, 
    and assign the resulting list to `data`
    - Assign the first position indexed at `0` in `data` to the variable `name`
    - Convert the remaining positions in `data` to a list of integers with loop variable `h`, 
    and assign the resulting list to `hours_list`
    - Calculate the total hours worked by the person by applying the `sum()` function to the `hours_list`, 
    and store the result in the `total_hours` dictionary with the `name` as the 
    key: `total_hours[name] = sum(hours_list)`
- return `total_hours`

## def min_max_hours(filename):
````
def min_max_hours(filename):
    """
    Find the minimum number of hours studied by each student.
    :param filename:
        keys are strings, representing student names
        values are list of integers, corresponding to the study hours
    :return: list of integers representing minimum number of hours studied by
        each student
    Example if `student_hours_d` is {'joe':[10,8,5,10], 'sue':[7,9,10]}
        the function returns [5,7]
    """
````
### Problem Solving Steps
- Look at file and indentify what names go with what hours
- read through hours for each person and identify the smallest amount in the list
- take the smallest hour for each person and put it into a list of just integers

### Computational Steps
- Begin an accumulation using an empty list `[]`, assigned as `min_hours`
- Open the file named `filename` using the `with ... as ...` statement and the `open()` function call,
and file object `f`
  - Iterate through the lines of the `file` using a `for` loop with loop variable `line`
    - Split each line into a list of fields using the `.split(',')` method, 
    and assign the resulting list to `data`
    - Convert the non-empty positions in `data` to a list of integers using loop variable `h`,
    and assign the resulting list to `hours_list` 
      - using `if` conditional, only include h in the list comprehension if it is not an empty string.
    - If `hours_list` is not empty, `append` the minimum value of `hours_list` to `min_hours` using 
    the `.append()` method and the `min()` function: `min_hours.append(min(hours_list))`
    - If `hours_list` is empty, append a `0` to `min_hours` using the `.append()` method: `min_hours.append(0)`
- return `min_hours`

