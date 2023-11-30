> More practice with files
### read_data() Function Design
```
def read_data(filename):
    """
    Read data from text file named `filename`. The file has lines of
    comma-separated strings, such that:
    - 1st string has info about a loan
    - 2nd string has info about the name of the country that got the loan
    - 3rd string has info about the time it took to raise the loan
    - 4th string has info about the number of lenders who contributed to the
        loan
    :param filename: string
    :return: list of dictionaries, each dictionary has 4 key-value pairs
        keys: 'loan', 'country', 'raising_time', 'lenders'
        values: strings, such that 1st string corresponds to 'loan' key,
            2nd string to 'country' key, 3rd to `raising_time` key, and
            4th string to 'lenders' key
    """
```

### Problem Solving Steps
- Open the text file with name `filename`
- Initialize an accumulator with an empty list
- Read each line in the file and make it into a dictionary 
- Add dictionary to a list

### Computational Steps
- Open the text file named `filename` using `with ... as ...` statement to 
  create `fin_obj` that gets hold of the content of the file
  - Call `readlines()` method on `fin_obj` to get a list of all lines in 
    the file 
  - Use an assignment to save the call into `lines_lst` variable of type 
    list of strings
- Initilize accumulator `d_list` of type list with empty list
- Use for loop to iterate through `lines_lst` with loop variable `line`
- At each iteration
  - strip '\n' from the end of the `line` using `rstrip('\n')`, and store 
    return value in `line`
  - split the `line` by comma, call `split(',')`, and store return value in
    `values_lst` 
  - To obtain a dictionary `line_d` from `values_lst`
    - Initialize witn empty dictionry `line_d`
    - Use 4 assignment statemnets to add key:value pair to `line_d`
      - Index `line_d` with the key ('loan', 'country', ...) and assign 
        corresonding value from `values_lst` at index 0, 1, ..
  - Append `lind_d` to `d_list`

