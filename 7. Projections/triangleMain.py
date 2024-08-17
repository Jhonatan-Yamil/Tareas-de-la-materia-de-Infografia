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
