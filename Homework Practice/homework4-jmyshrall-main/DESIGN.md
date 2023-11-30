> GeneratePassword Methods Design Document

### Constructor Method
```
def __init__(self, file_in, file_out='output.csv'):
        """
        Create Analysis object. Its instance variables have
        - the name of the input text file from where data is read
        - the name of the output text file where various outputs are right
        - the content of the input file.
        :param file_in: string        :param file_out:
        """
````
### Problem Solving Steps
- initialize the problem-solving process
- begin by reading through the given file

### Computational Steps
- Define instance variable `self.file_in` and initialize it with parameter 
  `file_in`
- Define instance variable `self.file_out` and initialize it with parameter 
  `file_out`
- use `with...open...as` to access `file_in`
  - define instance variable `self.Data` assigned as `f.readlines()`

### `transform_to_d()` Instance Method Design
```
  def transform_to_d(self):
        """
        Find the hours recorded for each student in `self.data`.
        :return: dictionary
            keys are strings, representing student names
            values are list of integers, corresponding to the study hours
        Example: If `self.data` has the content of 'data_2.csv`
            the method returns: {'joe':[10,8,5,10], 'sue':[7,9,10]}
        """
```
### Problem Solving steps
- Look at file and indentify what names go with what hours
- read through hours for each person and identify the smallest amount in the list
- take the smallest hour for each person and put it into a list of just integers

### Computational Steps
- Begin accumulation with blank dictionary `{}` assigned as `hours_dict`
- iterate through `self.Data` using loop variable `line`
  - call `.strip()` and `.split(',')` to separate each line and assign as `line_list`
  - assign `name` as the value in index 1 of `line_list`
  - assign `hours` as an `int` `x` for every value after index 0 
    - use `for` loop to iterate `x` through `line_list[1:]`
  - assign `hours_dict` as a key value pair with `name` and `hours`
- return `hours_dict`

### `avg_hours()` Instance Method Design
```
  def avg_hours(self, student_hours_d):
        """
        Find the average number of study hours for each student.
        :param student_hours_d: dictionary
            keys are strings, representing student names
            values are list of integers, corresponding to the study hours
        :return: dictionary, keys are student names, values are hour averages.
        Example: if `student_hours_d` is {'joe':[10,8,5,10], 'sue':[7,9,10]}
            the function returns {'joe':33, 'sue':26}
        """
```
### Problem Solving steps
- Look through file and see what names go to what hours
- take the names and their respective hours and avg the hours
- take name and put it with the total avg of their hours along with other names and their hours

### Computational Steps
- initiate iteration using blank dictionary `{}` assigned as `avg_dict`
- iterate through `student_hours_d.items` using 2 loop variables for the key and value `name` `hour`
  - at each iteration `sum` the `hours` and divide by the `len` of `hours` to get an average assign as `avg_dict[name]`
- return `avg_dict`


### `min_max_hours()` Instance Method Design
```
   def min_max_hours(self, student_hours_d):
        """
        Find the minimum number of hours studied by each student.
        :param student_hours_d:
            keys are strings, representing student names
            values are list of integers, corresponding to the study hours
        :return: list of integers representing minimum number of hours studied
            by each student
        Example if `student_hours_d` is {'joe':[10,8,5,10], 'sue':[7,9,10]}
            the function returns [5,7]
        """
```
### Problem Solving steps
- Look at file and indentify what names go with what hours
- read through hours for each person and identify the smallest amount in the list
- take the smallest hour for each person and put it into a list of just integers

### Computational Steps
- initialize an iteration using an empty list `[]` assigned as `min_list`
- iterate through `student_hours_d.values()` using loop variable `hours`
  - use `min(hours)` function at each iteration and `.append` each value to `min_list`
- return `min_list`

### `report_avg()` Instance Method Design
```
       def report_avg(self):
        """
        Write to `self.file_out` the average number of hours for each student.
        A line in the output file has the name of the student followed by
        one space and then the average number of hours.
        Example: if `self.data` had data from `data_2.csv`, the output file
        has the following content:
            joe 33
            sue 26
        """
```
### Problem Solving steps
- Look through file and see what names go to what hours
- take the names and their respective hours and avg the hours
- take name and put it with the total avg of their hours along with other names and their hours

### Computational Steps
- Call the `transform_to_d()` method of the `self` object, which returns a
dictionary `student_hours_d` containing the student names as keys and a list of their hours as values.
- Call the `avg_hours()` method of the `self` object, passing in `student_hours_d` as an argument. 
creating `avg_dict` containing the student names as keys and their average `hours` as values.
- Open a new file with the name `self.file_out` in write mode using the with statement.
- Loop through the items in the `avg_dict` dictionary using the `.items()` method.
- For each item, format a string containing the student `name` and average `hours` using an `f-string`, 
and write the string to the file using the `.write()` method. The string is formatted with the student `name` 
and average `hours` separated by a space, followed by a newline character.