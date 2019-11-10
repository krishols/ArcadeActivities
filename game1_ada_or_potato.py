
import arcade



# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"
GAME_SPEED = 1/60
TIMER_MAXIMUM = 100

NEXT_PHASE = {"nothing": "ada", "ada": "potato", "potato": "nothing"}

image_ada = arcade.load_texture("images/ada.png")
image_potato = arcade.load_texture("images/potato.png")


class AP(arcade.Sprite):
    phase: str
    timer: int

    def __init__(self):
        """ Initialize variables """
        super().__init__()
        self.phase = "nothing"
        self.timer = 0
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.texture = image_ada

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0
            self.phase = NEXT_PHASE[self.phase]

    def update_image(self):
        if self.phase == "ada":
            self.texture = image_ada
        else:
            self.texture = image_potato

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""


def main():
    window = AP()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
