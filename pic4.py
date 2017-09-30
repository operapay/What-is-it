import arcade
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
 
class background(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.COLUMBIA_BLUE)
        self.two = arcade.Sprite('images/two.png')
        self.two.set_position(190 , 370)
        self.bird = arcade.Sprite('images/bird.png')
        self.bird.set_position(120 , 370)      
        self.head = arcade.Sprite('images/head.png')
        self.head.set_position(270 , 370)       
        self.t1 = arcade.create_text("ส    อ    ก    ง     เ     บ    ก", arcade.color.BLACK, 20)
        self.t2 = arcade.create_text("ด็    ม    หั    น    ล    ว    ข", arcade.color.BLACK, 20)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(200,330,290,290, arcade.color.LIGHT_CYAN)
        for i in range(7):
            arcade.draw_rectangle_filled(110+30*i,270,25,30, arcade.color.QUEEN_BLUE)
        self.bird.draw() 
        self.two.draw() 
        self.head.draw()
        for j in range(7):
            arcade.draw_rectangle_filled(80+40*j,120,25,30, arcade.color.BUBBLES)
            for i in range(7):
                arcade.draw_rectangle_filled(80+40*i,70,25,30, arcade.color.BUBBLES)
        start_y = 60
        start_x = 70
        arcade.draw_point(start_x, start_y, arcade.color.BLUE, 1)
        arcade.render_text(self.t1, start_x, start_y)
        start_y2 = 110
        start_x2 = 70
        arcade.draw_point(start_x2, start_y2, arcade.color.BLUE, 1)
        arcade.render_text(self.t2, start_x2, start_y2)


if __name__ == '__main__':
    window = background(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()