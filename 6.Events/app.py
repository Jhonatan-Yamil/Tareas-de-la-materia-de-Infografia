import arcade
import random
from game_object import Polygon2D

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Polygon2d"


def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.objects = []

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            for obj in self.objects:
                obj.translate(10, 0)
        elif symbol == arcade.key.LEFT:
            for obj in self.objects:
                obj.translate(-10, 0)
        elif symbol == arcade.key.UP:
            for obj in self.objects:
                obj.translate(0, 10)
        elif symbol == arcade.key.DOWN:
            for obj in self.objects:
                obj.translate(0, -10)

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.objects.append(
                Polygon2D(
                    vertices=[
                        (x - 50, y - 50),
                        (x - 50, y + 50),
                        (x + 150, y + 50),
                        (x + 150, y - 50),
                    ],
                    color=get_random_color(),
                )
            )
            self.objects.append(
                Polygon2D(
                    vertices=[
                        (x, y+ 50 ),
                        (x, y + 150),
                        (x + 100, y + 150),
                        (x + 100, y + 50),
                    ],
                    color=get_random_color(),
                )
            )
            self.objects.append(
                Polygon2D(
                    vertices=[
                        (x+100, y+ 100 ),
                        (x+100, y + 125),
                        (x + 150, y + 125),
                        (x + 150, y + 100),
                    ],
                    color=get_random_color(),
                )
            )
            
            print(f"objetos: {len(self.objects)}")
        

    def on_draw(self):
        arcade.start_render()
        for obj in self.objects:
            obj.draw()


if __name__ == "__main__":
    app = App()
    arcade.run()