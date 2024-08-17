import arcade
import numpy as np
from game_object import Object3D

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Proyección 3D con Cabeza de Zorro que sigue el cursor, Jhonatan Yamil Cabezas"
ROTATION_SPEED = 0.01

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.GRAY)
        self.fox_head = Object3D(
            [
                (0.5, 1.5, 0.5),  # Oreja derecha superior 0
                (-0.5, 1.5, 0.5),  # Oreja izquierda superior 1
                (0.3, 1, 0.5),  # Oreja derecha inferior 2 
                (-0.3, 1, 0.5),  # Oreja izquierda inferior 3
                (0.7, 0.5, 0),  # Cabeza derecha superior 4
                (-0.7, 0.5, 0),  # Cabeza izquierda superior 5
                (0.7, -0.5, 0),  # Cabeza derecha inferior 6
                (-0.7, -0.5, 0),  # Cabeza izquierda inferior 7
                (0.2, 0, -0.5),  # Hocico derecho 8
                (-0.2, 0, -0.5),  # Hocico derecha 9
                (0.2, 0.6, -0.5), #Ojo derecho 10
                (-0.2, 0.6, -0.5), #Ojo izquierdo 11
                (0.2, -0.2, -0.5),  # Hocico derecho 12
                (-0.2, -0.2, -0.5),  # Hocico izquierdo 13
                
            ],
            [
                (0, 2), (1, 3),  # Orejas
                (2, 3),          # conexion Orejas de ambos lados
                (8, 9),          # Conexion hocicos
                # (6, 7),          # Conexion mentones
                (2, 4), (3, 5),  # Conexión orejas y cabeza
                (4, 6), (5, 7),  # Cabeza
                (6, 8), (7, 9),  # Conexión cabeza y hocico
                (8, 0), (9, 1),  # Nariz
                (12, 13),(9,13),(8,12), #Hocico completo
                (13, 7), (12,6),
            ],
            arcade.color.ORANGE
        )
        self.fox_head.translate(400, 400, 0) 
        self.fox_head.scale(200, 200, 200)   
        
        self.target_angle_x = 0  # Ángulo objetivo de rotación en X
        self.target_angle_y = 0  # Ángulo objetivo de rotación en Y

    def on_update(self, delta_time: float):
        
        if self.target_angle_x != 0 or self.target_angle_y != 0:
            self.fox_head.rotate(self.target_angle_y*ROTATION_SPEED, "y", pivot=self.fox_head.get_center())
            self.fox_head.rotate(self.target_angle_x*ROTATION_SPEED, "x", pivot=self.fox_head.get_center())

            # Evita rotaciones adicionales
            self.target_angle_x = 0
            self.target_angle_y = 0

        
    def on_draw(self):
        arcade.start_render()
        self.fox_head.draw()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        
        # Calcular el cambio en ángulo basado en la posición del cursor
        self.target_angle_y =-(x - SCREEN_WIDTH / 2) * ROTATION_SPEED
        self.target_angle_x = (y - SCREEN_HEIGHT / 2) * ROTATION_SPEED
if __name__ == "__main__":
    app = App()
    arcade.run()
