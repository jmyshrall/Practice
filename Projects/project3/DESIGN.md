> Project 2 Design Document

## password_8chars() Function Design
- **Input**: 3 strings `letters`, `caps`, `numbers`
  - a string of  lowercase letters
  - a string of uppercase letters
  - a string of decimal digit characters
- **Output**: a string, representing a password of 8 characters, chosen 
  randomly from the three 
  strings

### Problem Solving Steps
*How do we obtain the output from given input?*
- put `letters`, `caps`, `numbers` in a new string
- randomly select one character from each string 8 times
- make the password from these characters 

### Computational Steps
*Rewrite the problem-solving steps into computational steps. Use the 
accumulation pattern.*
- Concatenate `letters`, `caps`, `numbers` into `all_chars`
- Define the accumulator and assign it 
  - assign as `new_password`
  - initialize with empty string `'''`
- Do iteration
  - Use `for` loop to iterate 8 times `range(8)`
  - pick a random character `char` from `all_chars`
  - concatenate `char` to `new_password`
- return `new_password`

## password_4words() Function Design
- **Input**: 3 lists of words
  - a list of nouns, a list of verbs, a list of adjectives
- **Output**: a string, representing a password that concatenates 3 words, 
  each randomly selected from each of the lists

### Problem Solving Steps
*How do we obtain the output from given input?*
- put `nouns`, `verbs`, and `adj` in a new string
- randomly pick one word from each list 3 times
- output a password using one word from each list

### Computational Steps
*Rewrite the problem-solving steps into computational steps. Use the 
accumulation pattern.*
- Concatenate `nouns`, `verbs`, `adj` into `all_words`
- Define the accumulator and assign it 
  - assign as `new_password2`
  - initialize with empty string `"""`
- Do iteration
  - Use `for` loop to iterate 8 times `range(3)`
  - pick a random character `word` from `all_words`
  - concatenate `word` to `new_password2`
- return `new_password2`

## password_4words_better() Function Design
- **Input**: Same as the input for `password_4words()`
- **Output**: Same as the output for `password_4words()`, but some letters are replaced with number characters or 
special characters:
  - 'o' is replaced with '0'
  - 'l' is replaced  '!'
  - 'a' is replaced with '@'
  - 'e' is replaced with '3'
- Hint: Don't redo the work that `password_4words()` does. 

### Problem Solving Steps
*How do we obtain the output from given input?*
- put `nouns`, `verbs`, and `adj` in a new string
- replace common letters like vowels a,i,o,u with special characters and numbers
- randomly pick one word from each list 3 times
- output a password using one word from each list with replaced letters
### Computational Steps
*Rewrite the problem-solving steps into computational steps. Use the 
accumulation pattern.*
- Concatenate `nouns`, `verbs`, `adj` into `all_words`
- replace `o`,`l`,`a`,`e` with `0`,`!`,`@1`,`3`
- Define the accumulator and assign it
  - assign as `new_password3`
  - initialize with empty string `"""`
- Do iteration
  - Use `for` loop to iterate 8 times `range(3)`
  - pick a random character `word` from `all_words`
  - concatenate `word` to `new_password3`
- return `new_password3`
