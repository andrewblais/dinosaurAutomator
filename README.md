# Dinosaur Automator

A class to automate the Google Chrome Dinosaur Game. Completed for Professional Portfolio
Project: Assignment 13: Angela Yu 100 Days of Code -- "GUI Automation: Automate the
Google Dinosaur Game"

- [Python](https://www.python.org/)

- [PIL](https://pillow.readthedocs.io/en/stable/)

- [PyAutoGUI](https://github.com/asweigart/pyautogui)

_MIT License: Copyright (c) 2024- Andrew Blais_

---

Future updates will include:

- Include functionality to allow for browser already being open and game running.

- Consider closer analysis of game motion/acceleration and improvement thereby to
  algorithm controlling automations handling of acceleration. Include options for user
  to chose between different algorithms.

- Allow user to pass their screen resolution in kwargs and set dim_x and dim_y
  accordingly. Ensure all ints dependent on/related to screen resolution are not hard-
  coded but are ratios derived from initial user resolution input.

- Other things too...

---

### Documentation:

```requirements
```

_Docstrings for `main.py`:_

```bash
Help on class DinosaurAutomator in module __main__:

class DinosaurAutomator(builtins.object)
 |  A class to automate the Google Chrome Dinosaur Game.
 |
 |  This automator navigates the dinosaur through obstacles by jumping, leveraging
 |   pixel analysis to determine the timing of jumps and adjusting th gameplay
 |   strategy based on the speed of the game, which increases over time.
 |
 |   Attributes:
 |       img_grab_init (ImageGrab): Initial screen grab to determine screen dimensions.
 |       img_grab_init_data (PixelAccess): Pixel Access object for `img_grab_init`.
 |       img_grab_data (PixelAccess): Current screen pixel data.
 |       dim_x (int): Screen width.
 |       dim_y (int): Screen height.
 |       theme_x (int): X-coordinate determining the theme of the game (light or dark).
 |       theme_y (int): Y-coordinate for the same.
 |       theme_bool (bool): Flag for game theme. False for 'light', True for 'dark'.
 |       l_min_vals (list): Minimum L values for light and dark themes, respectively.
 |       l_max_vals (list): Maximum L values for light and dark themes, respectively.
 |       l_min (int): Current minimum L value based on theme.
 |       l_max (int): Current maximum L value based on theme.
 |       obst_x_min (int): Minimum X-coordinate to start checking for obstacles.
 |       obst_x_max_init (int): Initial maximum X-coordinate to check for obstacles.
 |       obst_x_max (int): Adjustable maximum X-coordinate for obstacle detection.
 |       jump_x_increment (int): Value to increase `obst_x_max` by, adapt to game speed.
 |       jump_turns_counter (int): Counter for number of jumps, to adjust `obst_x_max`.
 |       jump_turns_max (int): Number of jumps after which `obst_x_max` is increased.
 |       obst_y_min (int): Minimum Y-coordinate to check for obstacles.
 |       obst_y_max (int): Maximum Y-coordinate to check for obstacles.
 |       did_initial_jump (bool): Flag to check if the initial jump has been made.
 |       game_url (str): URL of the Dinosaur Game.
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initializes the DinosaurAutomator with default values and starts the game
 |       automation process.
 |
 |  game_engine(self)
 |      The main loop of the game automation, handling initial and subsequent jumps.
 |
 |  get_current_colors(self)
 |      Updates the current screen pixel data and adjusts the
 |       theme-based L values accordingly.
 |
 |  get_screen_dimensions(self)
 |      Captures the initial screen dimensions for reference in gameplay logic.
 |
 |  initial_img_grab(self)
 |      Captures an initial screenshot of the game screen, used for determining
 |       screen dimensions and initializing pixel data.
 |
 |  initial_jump(self)
 |      Performs the initial jump to start the game and sets the flag indicating
 |       the game has started.
 |
 |  locate_theme_pixel(self)
 |
 |  open_dinosaur_game(self)
 |      Opens the Google Chrome browser and navigates to the Dinosaur Game URL.
 |
 |  subsequent_gameplay(self)
 |      Handles gameplay after the initial jump by detecting obstacles and
 |      adjusting jump timing as the game speeds up.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  game_ignition()
 |      Starts the Dinosaur Game by simulating a spacebar press.
 |
 |  standardize_gui()
 |      Prepares the GUI by making the browser fullscreen and resetting zoom,
 |       to ensure consistent screen dimensions and element placements.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
```

---

## Created in completing an assignment for Angela Yu Course:

### **Day 94, Professional Portfolio Project [GUI Automation]**

#### **_Assignment 13: "Automate the Google Dinosaur Game"_**

Write Python code to play the Google Dinosaur Game.

- _assignment
  for [Angela Yu 100 Days of Code](https://www.udemy.com/course/100-days-of-code/)_

### **Assignment instructions:**

On Chrome, when you try to access a website and your internet is down, you see a little
dinosaur. (Apparently because dinosaurs have short arms and they "can't reach" your
website.

On this page, there is a hidden game, if you hit space bar you can play the T-rex run
game.

![Project Description Image](/static/project_description.jpg)

Alternatively you can access the game directly here:

previously: https://elgoog.im/t-rex/
now: https://elgoog.im/dinosaur-game/

You goal today is to write a Python script to automate the playing of this game. Your
program will look at the pixels on the screen to determine when it needs to hit the space
bar and play the game automatically.

You can see what it looks like when the game is automated with a bot:

previously: https://elgoog.im/t-rex/?bot
now: https://elgoog.im/dinosaur-game/?bot

You might want to look up these two packages:

https://pypi.org/project/Pillow/

https://pyautogui.readthedocs.io/en/latest/

---

### My Submission:

My project is viewable here: https://github.com/andrewblais/...

---

### **Questions for this assignment**

#### _Reflection Time:_

**_Write down how you approached the project._**

stuff

**_What was hard?_**

stuff

**_What was easy?_**

stuff

**_How might you improve for the next project?_**

stuff

**_What was your biggest learning from today?_**

stuff

**_What would you do differently if you were to tackle this project again?_**

stuff
