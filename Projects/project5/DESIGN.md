> Project 5 Design Document

## def line_count(filename):
``python
def line_count(filename):
    """
    Find and return the number of lines in the file named `filename`
    :param filename: string
    :return: non-negative integer
    """
``
### Problem Solving Steps
- Count each new line in the file

### Computational Steps
- Open the file named `file_name` using `with ... as ...` and `open()` function call,
and file object `f-in`
- Use `f-in.readlines()` to get a list of lines of text in the file, call it `lines_lst`
- define accumulator `total_line` of type `int`, initialized with 0
- use `for...in...` to iterate through `line_lst` with iterator `one_line`
  - at each iteration accumulate 1 into `total_lines`
- Return the accumulator `total_lines` 

## def country_count(filename):
````
def country_count(filename):
    """
    Find and return the number of countries in the file named `filename`. A
    country name starts at the beginning of a line in the file, ends with ':',
    and is separated from the rest of the characters in the line by a space.
    :param filename: string
    :return: mon-negative integer
    """
````

### Problem Solving Steps
- Look at each line in the text document
- Determine which one has a country listed and which does not
- count each line with a country as you go through list
- give a final total

### Computational Steps
- Begin an iteration called `count` as type `int` initialized at 0 
- Open the file named `file_name` using `with ... as ...` and `open()` function call,
and the file object `f_in`
- Iterate through `f_in` using a `for` loop with loop variable `line`
  - if `:` is found on a line
  - then add 1 to the integer of `count`
- return count

## def olympics_transform(filename):
````
def olympics_transform(filename):
    """
    Read and process the content of the text file `filename` to produce a tuple
    of 3 parallel lists. The first list has the name of the olympians, their
    age, and country of origin.
    :param filename: string
    :return: tuple of three parallel lists
        1st list is a list of strings, 2nd list is a list of integers, and
        3rd list is a list of strings.
    """
````
### Problem Solving Steps
- Go through text file identifying names, ages, and countries
- Place names in one list
- Place ages in another list
- Place countries in another list 
- add to each list going through the text file

### Computational Steps
- Create 3 empty lists `names`, `ages`, and `countries`
- Open the file named `file_name` using `with ... as ...` and `open()` function call,
and the file object `f_in`
- use `for` loop to iterate trough `f_in` using loop variable `line`
- assign variable `feilds` as each line of `filename` 
  - separate the text in `filename` using `split(',')`
- assign variable `name` indexed at position 0 of `feilds`
- assign variable `age` as type `int` indexed at position 2 of `feilds`
- assign variable `country` indexed at position 3 of `feilds`
  - append `name` to `names`
  - append `country` to `countries`
  - append `age` to `ages`
- Return `names`, `ages`, and `countries`

## def olympics_report(filename):
````
def olympics_report(filename):
    """
    Read and process the content of the text file named `filename` to produce
    a string with given formatting requirements. For each line in the file
    produce a string that has the following format:
        <name> is from <country> and competes in <sport>
        where <name>, <country>, and <sport> are strings found in the line of
        the file.
    :param filename: string
    :return: list of strings
    """
````
### Problem Solving Steps
- Go through text file identifying the names, country, and sports
- Assign a name to both a country and sport on the line
- Repeat for all lines of the text file
- Make a conclusion stating name, is from country, competes in sport

### Computational Steps
- Open the file named `filename` using `with ... as ...` and `open()` function call,
and file object `f_in`
- Use `f_in.readlines()` to get a list of lines of text in the file, call it `lines`
- Begin iteration with an empty list `report` to iterate through each line in `filename`
- Iterate through `lines` with loop variable `line`
  - assign variable `feilds` as each line of `filename`, separate the text in `filename` using `split(',')`
  - assign `name` as `feilds` indexed at 0
  - assign `country` as `feilds` indexed at 3
  - assign `sport` as `feilds` indexed at 4
  - append `name`, `country`, and `sport` to `report`
    - use f-string to concatenate each variable to a single statement in `report`
- Return `report`