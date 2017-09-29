import arcade
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
class background(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.COLUMBIA_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(200,370,300,320, arcade.color.LIGHT_CYAN)
        arcade.draw_rectangle_filled(200,600,400,80, arcade.color.ORANGE)
        arcade.draw_rectangle_filled(200,10,400,80, arcade.color.QUEEN_BLUE)

if __name__ == '__main__':
    window = background(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()