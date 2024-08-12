import arcade
from bresenham import get_line

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Lineas con bresenham, Jhonatan Yamil Cabezas Gomez"



class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 20
        self.origin_x = SCREEN_WIDTH // 2
        self.origin_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        arcade.start_render()
        x0 = 3
        y0 = -2
        x1 = 2
        y1 = 7
        points = get_line(x0, y0, x1, y1)
        self.draw_grid()
        self.draw_line_points(points, arcade.color.DARK_YELLOW)
        self.draw_scaled_line(x0, y0, x1, y1)

    def draw_grid(self):
        for v_l in range(-self.origin_x, self.origin_x, self.pixel_size):
            arcade.draw_line(
                v_l + self.origin_x, 
                0, 
                v_l + self.origin_x, 
                SCREEN_HEIGHT, 
                arcade.color.DARK_GRAY
            )

        for h_l in range(-self.origin_y, self.origin_y, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.origin_y, 
                SCREEN_WIDTH, 
                h_l + self.origin_y , 
                arcade.color.LIGHT_GRAY
            )

    def draw_line_points(self, points, color):
        for p in points:
            screen_x = p[0] * self.pixel_size + self.origin_x
            screen_y = p[1] * self.pixel_size + self.origin_y
            arcade.draw_point(screen_x, screen_y, color, self.pixel_size)

    def draw_scaled_line(self, x0, y0, x1, y1):
        #Para que desde el origen se vaya expandiendo hacia y se vea los 4 cuadrantes
        screen_x0 = x0 * self.pixel_size + self.origin_x
        screen_y0 = y0 * self.pixel_size + self.origin_y
        screen_x1 = x1 * self.pixel_size + self.origin_x
        screen_y1 = y1 * self.pixel_size + self.origin_y
        arcade.draw_line(
            screen_x0, 
            screen_y0, 
            screen_x1, 
            screen_y1,
            [100, 255, 40, 150],
            5
        )


if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()