import keyboard
from PIL import ImageGrab
import pyautogui as pg
import time


class DinosaurAutomator:
    """
    A class to automate the Google Chrome Dinosaur Game.

    This automator navigates the dinosaur through obstacles by jumping, leveraging
     pixel analysis to determine the timing of jumps and adjusting th gameplay
     strategy based on the speed of the game, which increases over time.

     Attributes:
         img_grab_init (ImageGrab): Initial screen grab to determine screen dimensions.
         img_grab_init_data (PixelAccess): Pixel Access object for `img_grab_init`.
         img_grab_data (PixelAccess): Current screen's pixel data.
         dim_x (int): Screen width.
         dim_y (int): Screen height.
         theme_x (int): X-coordinate determining the theme of the game (light or dark).
         theme_y (int): Y-coordinate for the same.
         theme_bool (bool): Flag for game's theme. False for 'light', True for 'dark'.
         l_min_vals (list): Minimum L values for light and dark themes, respectively.
         l_max_vals (list): Maximum L values for light and dark themes, respectively.
         l_min (int): Current minimum L value based on theme.
         l_max (int): Current maximum L value based on theme.
         obst_x_min (int): Minimum X-coordinate to start checking for obstacles.
         obst_x_max_init (int): Initial maximum X-coordinate to check for obstacles.
         obst_x_max (int): Adjustable maximum X-coordinate for obstacle detection.
         jump_x_increment (int): Value to increase `obst_x_max` by, adapt to game speed.
         jump_turns_counter (int): Counter for number of jumps, to adjust `obst_x_max`.
         jump_turns_max (int): Number of jumps after which `obst_x_max` is increased.
         obst_y_min (int): Minimum Y-coordinate to check for obstacles.
         obst_y_max (int): Maximum Y-coordinate to check for obstacles.
         did_initial_jump (bool): Flag to check if the initial jump has been made.
         game_url (str): URL of the Dinosaur Game.
    """

    def __init__(self):
        """
        Initializes the DinosaurAutomator with default values and starts the game
         automation process.
        """
        self.img_grab_init = None
        self.img_grab_init_data = None
        self.img_grab_data = None
        self.dim_x = 1920
        self.dim_y = 1080
        self.theme_x = 1650
        self.theme_y = 150
        self.theme_bool = False  # Determines the game theme (light or dark).
        self.l_min_vals = [76, 166]
        self.l_max_vals = [88, 178]
        self.l_min = 76
        self.l_max = 88

        self.obst_x_min = 250
        self.obst_x_max_init = 635
        self.obst_x_max = self.obst_x_max_init

        self.jump_x_increment = 2
        self.jump_turns_counter = 0
        self.jump_turns_max = 10

        self.obst_y_min = 510
        self.obst_y_max = 560
        self.did_initial_jump = False
        self.game_url = 'https://elgoog.im/dinosaur-game/'

        # Initialize game setup and execution:
        self.initial_img_grab()
        self.get_screen_dimensions()
        self.open_dinosaur_game()
        self.standardize_gui()
        self.locate_theme_pixel()
        self.game_ignition()
        self.game_engine()

    def game_engine(self):
        """
        The main loop of the game automation, handling initial and subsequent jumps.
        """
        while not self.did_initial_jump:
            self.get_current_colors()
            self.initial_jump()
        while True:
            self.get_current_colors()
            self.subsequent_gameplay()

    def initial_jump(self):
        """
        Performs the initial jump to start the game and sets the flag indicating
         the game has started.
        """
        if keyboard.is_pressed('q'):
            quit()

        for x in range(630, 650):
            if self.l_min < self.img_grab_data[x, 575] < self.l_max:
                pg.press('space', presses=10, interval=0.05)
                self.did_initial_jump = True
                return

    # Account for acceleration by adding to x-vals every second?
    def subsequent_gameplay(self):
        """
        Handles gameplay after the initial jump by detecting obstacles and
        adjusting jump timing as the game speeds up.
        """
        if keyboard.is_pressed('q'):
            quit()

        for x in range(self.obst_x_min, int(self.obst_x_max)):
            for y in range(500, 575):
                if self.l_min < self.img_grab_data[x, y] < self.l_max:
                    pg.press('space')
                    self.jump_turns_counter += 5
                    if self.jump_turns_counter == self.jump_turns_max:
                        self.obst_x_max += self.jump_x_increment
                        self.obst_x_max = min(self.obst_x_max, self.dim_x)
                        self.jump_turns_counter = 0
                    return

        # Detects 'Game Over' banner, resets x_accel variables and resumes:
        if self.l_min < self.img_grab_data[1015, 350] < self.l_max:
            self.obst_x_max = self.obst_x_max_init
            self.jump_turns_counter = 0
            pg.press('space')
            return

    def get_current_colors(self):
        """
        Updates the current screen's pixel data and adjusts the
         theme-based L values accordingly.
        """
        self.img_grab_data = ImageGrab.grab().convert('L').load()
        self.theme_bool = self.img_grab_data[self.theme_x, self.theme_y] < 150
        self.l_min = self.l_min_vals[self.theme_bool]
        self.l_max = self.l_max_vals[self.theme_bool]

    @staticmethod
    def standardize_gui():
        """
        Prepares the GUI by making the browser fullscreen and resetting zoom,
         to ensure consistent screen dimensions and element placements.
        """
        pg.press('f11')  # Make browser fullscreen
        time.sleep(1)
        pg.hotkey('ctrl', 'num0')  # Reset zoom on browser
        time.sleep(1)

    def get_screen_dimensions(self):
        """Captures the initial screen dimensions for reference in gameplay logic."""
        self.dim_x, self.dim_y = self.img_grab_init.size

    def locate_theme_pixel(self):
        self.theme_x, self.theme_y = self.dim_x / 1.16, self.dim_y / 7.2
        pg.moveTo(self.theme_x, self.theme_y)  # Move cursor away from game action
        time.sleep(1)

    def open_dinosaur_game(self):
        """Opens the Google Chrome browser and navigates to the Dinosaur Game URL."""
        pg.press('win')
        time.sleep(1)
        pg.write('chrome')
        time.sleep(1)
        pg.press('enter')
        time.sleep(3)  # Allow Chrome to load
        pg.write(self.game_url)
        pg.press('enter')
        time.sleep(3)  # Wait for game to load

    @staticmethod
    def game_ignition():
        """Starts the Dinosaur Game by simulating a spacebar press."""
        pg.press('space')  # Begin game!

    def initial_img_grab(self):
        """
        Captures an initial screenshot of the game screen, used for determining
         screen dimensions and initializing pixel data.
        """
        self.img_grab_init = ImageGrab.grab().convert('L')
        self.img_grab_init_data = self.img_grab_init.load()


if __name__ == "__main__":
    help(DinosaurAutomator)
    # dinosaur_automator = DinosaurAutomator()
    # dinosaur_automator.game_ignition()
