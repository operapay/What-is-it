import arcade
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
 
class background(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.COLUMBIA_BLUE)
        self.cat = arcade.Sprite('images/cat.png')
        self.cat.set_position(190 , 370)
        self.baby = arcade.Sprite('images/baby.png')
        self.baby.set_position(120 , 370)      
        self.water = arcade.Sprite('images/water.png')
        self.water.set_position(270 , 370)       

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(200,330,290,290, arcade.color.LIGHT_CYAN)
        for i in range(7):
            arcade.draw_rectangle_filled(110+30*i,270,25,30, arcade.color.QUEEN_BLUE)
        self.cat.draw() 
        self.baby.draw() 
        self.water.draw()

if __name__ == '__main__':
    window = background(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()