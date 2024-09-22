import pytest
import logging

# Create a logger that writes to a file
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('test_rhombus_figure.log')
handler.setLevel(logging.INFO)
logger.addHandler(handler)

from lesson_15.romb_figure import Rhombus


class TestRhombus:
    def test_rhombus_creation(self):
        logger.info("Testing Rhombus creation")
        rhombus = Rhombus(5, 60)
        assert rhombus.side_a == 5
        assert rhombus.angle_a == 60
        assert rhombus.angle_b == 120
        logger.info("Rhombus creation test passed")

    def test_rhombus_invalid_side_length(self):
        logger.info("Testing Rhombus creation with invalid side length")
        with pytest.raises(ValueError):
            Rhombus(0, 60)
        logger.info("Rhombus creation with invalid side length test passed")

    def test_rhombus_str_representation(self):
        logger.info("Testing Rhombus string representation")
        rhombus = Rhombus(5, 60)
        assert str(rhombus) == "Rhombus(side_a=5, angle_a=60, angle_b=120)"
        logger.info("Rhombus string representation test passed")

    def test_rhombus_invalid_angle(self):
        logger.info("Testing Rhombus creation with invalid angle")
        with pytest.raises(ValueError):
            Rhombus(5, 200)
        logger.info("Rhombus creation with invalid angle test passed")

    def test_rhombus_set_attr(self):
        logger.info("Testing Rhombus set_attr method")
        rhombus = Rhombus(5, 60)

        # Change side and angle
        rhombus.set_attr('side_a', 10)
        rhombus.set_attr('angle_a', 45)

        # Validate changes
        assert rhombus.side_a == 10
        assert rhombus.angle_a == 45
        assert rhombus.angle_b == 135

        logger.info("Rhombus set_attr method test passed")