import arcade
import numpy as np
import random
from game_object import Object3D

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Projeccion 3d"


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
        self.cube = Object3D(
            [
                (1, 1, 1),
                (1, 1, -1),
                (1, -1, 1),
                (1, -1, -1),
                (-1, 1, 1),
                (-1, 1, -1),
                (-1, -1, 1),
                (-1, -1, -1),
            ],
            [
                (0, 1),
                (1, 3),
                (2, 3),
                (2, 0),
                (4, 5),
                (5, 7),
                (6, 7),
                (6, 4),
                (0, 4),
                (1, 5),
                (2, 6),
                (3, 7)
            ],
            arcade.color.YELLOW
        )
        self.cube.translate(399, 399, 0)
        self.cube.scale(100, 100, 100)
        self.cube.rotate(0.1, "x")
        self.cube.rotate(0.3, "y")
        self.cube.rotate(0.1, "z")
    
    def on_update(self, delta_time: float):
        self.cube.rotate(delta_time, "y")
        pass

    def on_draw(self):
        arcade.start_render()
        self.cube.draw()

    # def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        # self.cube.rotate(y, "x")
        # self.cube.rotate(x, "y")
        # self.cube.rotate(z, "z")
    
if __name__ == "__main__":
    app = App()
    arcade.run()



import arcade
import numpy as np
import random
from game_object import Object3D

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Proyección 3D con Triángulo que sigue el cursor"
class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        # Definir un triángulo en 3D
        self.triangle = Object3D(
            [
                (0, 1, 0),
                (-1, -1, 0),
                (1, -1, 0)
            ],
            [
                (0, 1),
                (1, 2),
                (2, 0)
            ],
            arcade.color.YELLOW
        )
        self.triangle.translate(400, 400, 0)
        self.triangle.scale(100,100,100)

    def on_update(self, delta_time: float):
        pass 
    def on_draw(self):
        arcade.start_render()
        self.triangle.draw()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        # Calcular el ángulo entre el vértice superior y la posición del cursor
        vx, vy, _ = self.triangle.vertices[0]
        angle = np.arctan2(y - vy, x - vx)

        # Rotar el triángulo alrededor de su centro en el eje Z
        self.triangle.rotate(angle, "z", pivot=self.triangle.get_center())
    
if __name__ == "__main__":
    app = App()
    arcade.run()
