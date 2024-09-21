import logging

# Configure the logger to write to a file
logging.basicConfig(filename='romb_figure.log', level=logging.INFO)

class Rhombus:
    def __init__(self, side_a, angle_a):
        self.logger = logging.getLogger()  # Get the root logger
        if side_a <= 0:
            raise ValueError("Side length must be greater than 0")
        if angle_a <= 0 or angle_a >= 180:
            raise ValueError("Angle must be between 0 and 180 degrees")
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a
        self.logger.info("Rhombus instance created successfully")

    def __str__(self):
        return f"Rhombus(side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b})"

# Create a Rhombus instance
rhombus = Rhombus(5, 60)