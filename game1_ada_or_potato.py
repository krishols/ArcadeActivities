import arcade

# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"
GAME_SPEED = 1 / 60
TIMER_MAXIMUM = 100

NEXT_PHASE = {"nothing": "ada", "ada": "potato", "potato": "nothing"}

image_ada = arcade.load_texture("images/ada.png")
image_potato = arcade.load_texture("images/potato.png", scale=.2)


class AP(arcade.Sprite):
    phase: str
    timer: int
    score=0
    def __init__(self):
        """ Initialize variables """
        super().__init__()
        self.phase = "ada"
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

    def switch_image(self):
        if self.timer <= 50:
            self.texture = image_potato
        else:
            self.texture = image_ada

    def update(self):
        self.update_timer()
        self.switch_image()

    def add_score(self):
        self.score += 1
        print(self.score)

    def lose_score(self):
        self.score -= 1
        print(self.score)

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()


class APGame(arcade.Window, AP):

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.logo_list = None

    def setup(self):
        arcade.set_background_color(BACKGROUND_COLOR)
        self.logo_list = arcade.SpriteList()
        self.logo_list.append(AP())

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.logo_list.draw()
        arcade.draw_text(str(self.logo_list[0].score), 50, 50, arcade.color.WHITE_SMOKE, 14)

    def on_update(self, delta_time):
        self.logo_list.update()

    def on_mouse_press(self, x, y, button, modifiers):
        for logo in self.logo_list:
            if logo.texture == image_ada:
                logo.add_score()
            elif logo.texture == image_potato:
                logo.lose_score()




def main():
    window = APGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
