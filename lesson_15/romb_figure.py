import logging

# Configure the logger to write to a file
logging.basicConfig(filename='rhombus_figure.log', level=logging.INFO)


class Rhombus:
    def __init__(self, side_a, angle_a):
        self.logger = logging.getLogger()  # Get the root logger

        # Validate side and angle
        if side_a <= 0:
            self.logger.error("Side length must be greater than 0")
            raise ValueError("Side length must be greater than 0")
        if angle_a <= 0 or angle_a >= 180:
            self.logger.error("Angle must be between 0 and 180 degrees")
            raise ValueError("Angle must be between 0 and 180 degrees")

        # Set attributes using setattr
        setattr(self, 'side_a', side_a)
        setattr(self, 'angle_a', angle_a)
        setattr(self, 'angle_b', 180 - angle_a)  # Complementary angle

        # Log successful creation
        self.logger.info(f"Rhombus created with side_a={side_a}, angle_a={angle_a}, angle_b={180 - angle_a}")

    # Additional method to set attributes
    def set_attr(self, name, value):
        if name == 'side_a':
            if value <= 0:
                self.logger.error("Side length must be greater than 0")
                raise ValueError("Side length must be greater than 0")
        elif name == 'angle_a':
            if value <= 0 or value >= 180:
                self.logger.error("Angle must be between 0 and 180 degrees")
                raise ValueError("Angle must be between 0 and 180 degrees")
            setattr(self, 'angle_b', 180 - value)  # Update complementary angle
        setattr(self, name, value)
        self.logger.info(f"Attribute {name} set to {value}")

    def __str__(self):
        return f"Rhombus(side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b})"


# Create a Rhombus object
try:
    rhombus = Rhombus(5, 60)
    print(rhombus)

    # Modify attributes using the additional method
    rhombus.set_attr('side_a', 10)
    rhombus.set_attr('angle_a', 45)

    print(rhombus)
except ValueError as e:
    logging.error(f"Error: {e}")