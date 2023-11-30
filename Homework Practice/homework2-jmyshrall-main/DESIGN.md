> Homework 2 Design Document

## how_often() Function Design

### Problem Solving Steps
*Write here the problem-solving steps*
- identify the given list of courses and read each course
- identify which course is being counted `comp`,`math`, etc
- go through the list and identify each time the given subject occurs
- write the number of time the given course is in the given list

### Computational Steps
*Describe the problem-solving steps in terms of computational steps*
- assign a list `subject-log` with items that refer to courses
- assign a `course` whose value will be output 
- begin an accumulation with `count` starting at 0
- create a `for` loop checking the `subject_log` for `subject`
- append the amount of times `subject` is found to `result`
- return `result`
- print final `result`

## subject_study_hours() Function Design

### Problem Solving Steps
*Write here the problem-solving steps*
- identify the list of `subjects` and see how many `hours` for each `subject`
- identify which `subject` is being evaluated
- add total `hours` for evaluated subject
- state amount of `hours` calculated

### Computational Steps
*Describe the problem-solving steps in terms of computational steps*
- define all parameters for `subject_log`, `log_hours`, and `subject`
- make these items of `subject_study_hours` using `()`
- initialize a loop for `result` at 0 with loop variable `i`
- loop over indices of `subject_log` list with `range()`
- check if the index `subject_log` matches `subject` using `==`
- if there is a match add the index of `hour_log` to `result`
- return `result`
- print `result`

## most_hours() Function Design

### Problem Solving Steps
*Write here the problem-solving steps*
- identify a list of `subjects` and see how many `hours` for each `subject`
- determine which subject has the highest value of `hours`
- state which `subject` had the most `hours`

### Computational Steps
*Describe the problem-solving steps in terms of computational steps*
- begin an iteration using `max_hours` initialize with 0
- make `result` a blank string
- iterate using `for` over `range(len(subject_log))` to access current `subject` and `hour`
- check if `hour_log` > 0, 0 is `max_hours` 
- if `hour_log` passes `max_hours` changes to current `hour_log` and `result` changes `subject`
- `for` iterates this for every value in `subject_log` to find largest `hour`
- return `result`
- print `result`
