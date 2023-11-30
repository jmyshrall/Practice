# Lab3 Design Document

## Increment 1: Creating the First Alien

### New Programming Concepts and Techniques 

1) **Superclass Inheritance**: I learned about superclass inheritance by using the `super()`
function to inherit attributes and methods from the Sprite class, which is a built-in Pygame 
class for managing game elements.

2) **Updating Screen**: To display the alien on the screen, I had to call the `blitme()`method of the Alien class 
within the `update_screen()` function. This ensured that the alien was drawn correctly on the screen.

### Challenges and Solutions

1) **Updating the Screen**: To ensure that the alien appeared correctly on the screen, 
I had to make sure that the blitme() method was called in the correct order within the 
`update_screen()` function.

2) **Understanding Class Structure**: The structure of the `Alien` class and how it relates to the rest of the game 
was initially confusing. To overcome this, I carefully reviewed the code, compared it with the `Ship` class, 
and read relevant documentation.

### Future Learning Goals

1) **Game Logic**: Understanding the logic behind game development, such as alien movement patterns, collision detection,
and scoring systems, is an area I want to delve deeper into as I continue working on this project.

## Increment 2: Building the Alien Fleet

### New Programming Concepts and Techniques 

1) **Refactoring Functions**: The code demonstrates the importance of refactoring by breaking down complex tasks 
into smaller, more manageable functions. It introduces functions like `get_number_aliens_x()` and `create_alien()`
to improve code readability and maintainability.

2) **Creating Rows of Aliens**: The code creates a group called aliens to hold all the alien instances. 
It also introduces a function called `create_fleet()` that is responsible for generating a full fleet of aliens. 
To create multiple rows of aliens, the code uses nested loops, with the outer loop controlling the number of rows and 
the inner loop creating aliens in each row.

### Challenges and Solutions

1) **Code Refactoring**: Refactoring the code to make it more modular and readable was essential. 
This involved creating new functions to handle specific tasks, which improved code organization 
and made it easier to maintain.

### Future Learning Goals

1) **Collision Detection**: Implementing collision detection between bullets fired by the ship and the alien fleet 
is a critical aspect of gameplay. I aim to learn more about collision detection algorithms and how to handle 
collisions effectively.

## Increment 3: Making the Fleet Move

### New Programming Concepts and Techniques 

1) **Alien Speed Settings**: It introduced a new setting, `alien_speed_factor`, 
to control the horizontal speed of the aliens. This setting determines how quickly 
the aliens move from one side of the screen to the other.

2) **Fleet Direction Setting**: It introduced the `fleet_direction` setting, which takes values of 1 or -1 to
represent the direction of the alien fleet. A value of 1 indicates movement to the right, 
while -1 indicates movement to the left.

### Challenges and Solutions

1) **Changing Fleet Direction**: To change the direction of the fleet when an edge is reached, 
I created the `change_fleet_direction()` function. This function updated the positions of all aliens 
in the fleet and adjusted the `fleet_direction` setting. As well as utilizing code from the master file on GitHub.

### Future Learning Goals

1) **Game Logic**: Implementing game logic, such as scoring and game over conditions as they are
essential for creating a complete and engaging game experience. I aim to explore these aspects in detail.

## Increment 4: Shooting Aliens

### New Programming Concepts and Techniques 

1) **Handling Collisions**: The code in `check_bullet_alien_collisions()` is responsible for checking 
bullet-alien collisions, updating the game state when collisions occur, 
and creating a new fleet of aliens when the current fleet is destroyed.

2) **Refactoring**: I refactored the `update_bullets()` function to improve code organization and readability. 
The code for checking bullet-alien collisions was moved to a separate function, 
`check_bullet_alien_collisions()`, making the main update function cleaner and more focused.

### Challenges and Solutions

1) **Handling Multiple Tasks**: By refactoring the `update_bullets()` function and moving the collision 
handling code to `check_bullet_alien_collisions()`, I improved code organization and readability 
while keeping tasks separate and manageable.

### Future Learning Goals

1) **Scoring System**: Implementing a scoring system to keep track of the player's score when 
shooting down aliens would enhance the gameplay experience.

2) **Adding a Start Button**: Implementing a start button is not necessary, but it is an important staple 
in any game design by allowing the functions not to run unless permitted. 

## Increment 5: Ending the Game

### New Programming Concepts and Techniques 

1) **Ending the Game**: The game can now be ended by setting the `game_active` attribute to `False` in the 
`GameStats` class when certain conditions are met, such as when the player runs out of ships.

2) **Checking for Aliens at the Bottom**: I created the `check_aliens_bottom()`
function to check if any aliens have reached the bottom of the screen. When an alien reaches the bottom, 
it is treated as if it hit the ship which is a new fail condition. 

### Challenges and Solutions

1) **Implementing Game Over**: I introduced the concept of a game over state by using the 
`game_active` flag in the `GameStats` class. When the player runs out of ships, 
the game transitions to a game over state.

### Future Learning Goals

1) **Sound and Visual Effects**: Adding sound effects and visual effects for events like alien-ship 
collisions or game over events can make the game more immersive.

## Conclusion

### Time and Approach

1) The overall project took a few hours, many were spent reformation and refactoring code. 
I found it help to do one increment of code then write the design doc for it. Rather than do each separately. 

### Collaboration

1) There was no collaboration for this lab, however it would have been useful to do so. As it allows me
to compare my formatting to another person to quickly see where errors would occur. 

### Lesson Learned 

1) One valuable lesson learned during this experience is the importance of breaking down complex projects into smaller,
manageable tasks. Incremental development not only helps in managing the workload effectively 
but also provides a sense of accomplishment as you complete each task. It also allows for more focused learning on
specific concepts before moving on to the next.