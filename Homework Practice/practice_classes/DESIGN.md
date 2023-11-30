> GeneratePassword Methods Design Document

### Constructor Method
```python
def __init__(self, password='********'):
    """
    Create object with password instance variable set up to "password"
    """
```

### Computational Steps
- Define instance varaible `self.password` and initilaize it with parameter 
  `password`

### `simple_pass()` Instance Method Design
```python

def simple_pass(self):
    """
    Create an 8-character passowrd composed of randoma digits, lower-case 
    letters, and upper-case letters, from the three class variables 
    `letters`, `caps`, and `numbers`. Assign it to instance variable
    `self.password`. 
      """
```
### Computational Steps
- Concatenate `letters`, `caps`, `numbers` into `all_chars`
- Define the accumulator and assign it 
  - assign as `new_password`
  - initialize with empty string `''`
- Do iteration
  - Use `for` loop to iterate 8 times `range(8)`
  - pick a random character `char` from `all_chars`
  - concatenate `char` to `new_password`
- assign `new_password` to `self.password`

### `word_pass()` Instance Method Design
```python
def word_pass(self):
    """
    Create a password by concatenating random words from the three
    class variable `nouns`, `adjectives`, and `verbs`. 
    Assign it to the instance variable `self.password`. 
    """
```
- Concatenate `GeneratePassword.nouns`, `GeneratePassword.verbs`, 
`GeneratePassword.adj` into `all_words`
- Define the accumulator and assign it 
  - assign as `new_password`
  - initialize with empty string `"""`
- Do iteration
  - Use `for` loop to iterate 3 times `range(3)`
  - pick a random character `word` from `all_words`
  - concatenate `word` to `new_password2`
- assign `new_password` to `self.password`

### `word_pass_better()` Instance Method Design
```python
def word_pass_better(self):
    """
    Call `self.word_pass()` to get a password by concatenating random 
    words from the class variables. Modify the returned value to be 
    capitalized and to have digits replacing certain leters
        e.g., 1 replaces l, 0 replaces o, and 3 replaces e
    Assign it to the instance variable `self.password`. 
    """
```
- Concatenate `GeneratePassword.nouns`, `GeneratePassword.verbs`,
`GeneratePassword.adj` into `all_words`
- replace `o`,`l`,`a`,`e` with `0`,`!`,`@1`,`3`
- Define the accumulator and assign it
  - assign as `new_password`
  - initialize with empty string `"""`
- Do iteration
  - Use `for` loop to iterate 3 times `range(3)`
  - pick a random character `word` from `all_words`
  - concatenate `word` to `new_password`
- assign `new_password` as `self.password`


