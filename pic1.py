import arcade
 
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 320
 
class background(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.LIGHT_CYAN)

    def on_draw(self):
        arcade.start_render()
        for i in range(7):
            arcade.draw_rectangle_filled(60+30*i,100,25,30, arcade.color.QUEEN_BLUE)

if __name__ == '__main__':
    window = background(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()