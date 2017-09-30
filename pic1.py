import arcade
 
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 320
 
class background(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.LIGHT_CYAN)
        self.cat = arcade.Sprite('images/cat.png')
        self.cat.set_position(140 , 200)
        self.baby = arcade.Sprite('images/baby.png')
        self.baby.set_position(80 , 200)      
        self.water = arcade.Sprite('images/water.png')
        self.water.set_position(210 , 200)       

    def on_draw(self):
        arcade.start_render()
        for i in range(7):
            arcade.draw_rectangle_filled(60+30*i,100,25,30, arcade.color.QUEEN_BLUE)
        self.cat.draw() 
        self.baby.draw() 
        self.water.draw()

if __name__ == '__main__':
    window = background(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()