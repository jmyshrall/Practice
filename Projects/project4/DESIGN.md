> Homework 4 Design Document

##  Function Design sessions_by_subject(study_log)

### Problem Solving Steps
*Write here the problem-solving steps*
- count how many times a subject is in the log
- use a tally to keep track of how many times a subject is in a log
- If the subject is not in the tally, add the subject and set its tally to 1 
- otherwise add 1 to the subject tally 

### Computational Steps
*Describe the problem-solving steps in terms of computational steps*
- use the histogram pattern (which is a special case of accumulation). The accumulator is a dictionary
- keys in the dictionary are the subjects
- values are the frequencies of the subjects

Step 1: set up the accumulation
- define variable `tally` of type `dict` and initialize it with `{}`

Step 2: Iterate through `study_log` with loop variable `subject`
- at each iteration step use conditional to check if `subject` is in `tally`
- if true, add `subject` key with value 1
- else increment value of `subject` by 1

Step 3: Return `tally`

## session_total(study_log_d) Function Design

### Problem Solving Steps
*Write here the problem-solving steps*
- Identify a list of classes with associated study times
- Add the amount of hours from the first class to the next class
- Repeat for all given classes and times
- Have a final value of the total hours

### Computational Steps
*Describe the problem-solving steps in terms of computational steps*
- use the histogram pattern (which is a special case of accumulation). The accumulator is a dictionary
- keys in the dictionary are the subjects
- values are the frequencies of the subjects

Step 1: set up the accumulation
- define variable `total_sessions` as type `int` initialized at `0`

Step 2: Iterate through `study_log_d` with loop variable `sessions`
- use `.values()` method to extract values from `study_log_d` dictionary
- add values from `study_log_d` to an `int` assigned as `total_sessions`

Step 3: Return `total_sessions`

## most_studied(study_log_d) Function Design

### Problem Solving Steps
*Write here the problem-solving steps*
- Identify a list of subjects and the amount of hour for each
- Note the amount of hours for the first subject see if the next subject has more
- If not only have the first subject in a list
- If next subject has more remove first subject and replace it with the next subject
- repeat for all values in list and if classes in max have same hours then both are in list

### Computational Steps
*Describe the problem-solving steps in terms of computational steps*
- use the histogram pattern (which is a special case of accumulation). The accumulator is a dictionary
- keys in the dictionary are the subjects
- values are the frequencies of the subjects

Step 1: set up an accumulation 
- initialize `max_sessions` as type `int` with `0`
- Create an empty list `most_studied_subjects` using `[]`
- loop through `study_log_d` using `.items()` to get a `tuple` of the pairs in the dictionary
- using two loop variables `subjects` and `sessions` to unpack the `tuple`

Step 2: Iterate through `study_log_d`
- if `sessions` is greater than `max_sessions` then update value of max to `sessions`
- update list `most_studied_subjects` searching through the dictionary using the current `subject` to index
  - elif `sessions` equal to `max_sessions` 
  - then append current iteration subject to `most_studied_subjects`
  
Step 3: Return `most_studied_subjects`

## subjects_by_session_numbers(study_log_d) Function Design

### Problem Solving Steps
*Write here the problem-solving steps*
- identify a list of subjects by assigned values of sessions
- go through the list assigning the value of sessions to the subject in a list
- if two subjects share the same value of session put subjects in same list
- final list should be a few lists with values of sessions assigned to them

### Computational Steps
*Describe the problem-solving steps in terms of computational steps*
- use the histogram pattern (which is a special case of accumulation). The accumulator is a dictionary
- keys in the dictionary are the subjects
- values are the frequencies of the subjects

Step 1: Set up an accumulation
- define variable `result` of type `dict` and initialize it with `{}`

Step 2: iterate through `study_log_d`
- Use `.items()` to iterate through the keys and values of `study_log_d`
- Use two loop variables `subject` and `sessions` to iterate for the keys and values of `study_log_d`
  - if current `session` is in `result`
    - then current `subject` is appended to the key value in the `result` dict as a separate `item`
  - else the current `session` is paired with the current `subject` in a separate `item`

Step 3: Return `result`