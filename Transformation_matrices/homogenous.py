import arcade
import arcade.color
import math
import numpy as np

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Matrices de transformacion"
AMPLITUDE = 5 
SPEED = 100
ROTATION_SPEED = 90

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.vertices = [(0, 350), (0, 450), (100, 450), (100, 350)]
        self.time=0
        self.direction=1
        self.rotation = 0
        
    def on_update(self, delta_time: float):
        self.time += delta_time
        dx = SPEED * delta_time * self.direction
        dy = AMPLITUDE * np.sin(self.time * 2) 
        self.vertices = self.translate(self.vertices, dx, dy)
        # Rotación continua
        self.rotation += ROTATION_SPEED * delta_time
        self.vertices = self.rotate(self.vertices, ROTATION_SPEED * delta_time)
        
        # Obtener el centro actual de la figura
        center_x, _ = self.get_center(self.vertices)
        
        # Cambiar dirección si se llega a los bordes
        if center_x < 0 or center_x > SCREEN_WIDTH:
            self.direction *= -1  # Invierte la dirección
    def on_draw(self):
        arcade.start_render()
        self.draw_shape(self.vertices)
        # print(self.vertices, self.get_center(self.vertices))
        # new = self.scale(self.vertices, 2.5)
        # self.draw_shape(new)
    def translate(self, vertices, dx, dy):
        TM = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
        return self.apply_transform(vertices, TM)
    
    def rotate(self, vertices, angle):
        angle_rad = np.radians(angle)
        xc, yc = self.get_center(vertices)
        # mover al origen
        T1 = np.array([
            [1, 0, -xc],
            [0, 1, -yc],
            [0, 0, 1]
        ])
        TM = np.array([
            [np.cos(angle_rad), -np.sin(angle_rad), 0],
            [np.sin(angle_rad), np.cos(angle_rad), 1],
            [0, 0, 1],
        ])
        T2 = np.array([
            [1, 0, xc],
            [0, 1, yc],
            [0, 0, 1]
        ])
        new_TM = np.dot(T2, np.dot(TM, T1))
        return self.apply_transform(vertices, new_TM)

    def scale(self, vertices, s):
        xc, yc = self.get_center(vertices)
        # mover al origen
        T1 = np.array([
            [1, 0, -xc],
            [0, 1, -yc],
            [0, 0, 1]
        ])
        TM = np.array([
            [s, 0, 0],
            [0, s, 0],
            [0, 0, 1]
        ])
        T2 = np.array([
            [1, 0, xc],
            [0, 1, yc],
            [0, 0, 1]
        ])
        new_TM = np.dot(T2, np.dot(TM, T1))
        return self.apply_transform(vertices, new_TM)
    
    def apply_transform(self, vertices, TM):
        v_array = np.array([[x, y, 1] for x, y in vertices])
        v_array = np.transpose(v_array)
        # apply transformation
        new_v_array = np.dot(TM, v_array)
        new_v_array = new_v_array[:2, :]
        new_v_array = np.transpose(new_v_array)
        new_v_list = new_v_array.tolist()
        return new_v_list
    
    def get_center(self, vertices):
        return np.mean(np.array(vertices), axis=0)
    
    def draw_shape(self, vertices):
        for x, y in vertices:
            arcade.draw_point(x, y, arcade.color.RED, 4)

        arcade.draw_line_strip(vertices+[vertices[0]], arcade.color.RED)


    
if __name__ == "__main__":
    app = MyWindow()
    arcade.run()