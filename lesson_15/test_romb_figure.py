import pytest
import logging

# Create a logger that writes to a file
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('test_romb_figure.log')
handler.setLevel(logging.INFO)
logger.addHandler(handler)

from lesson_15.romb_figure import Rhombus

def test_rhombus_creation():
    logger.info("Testing Rhombus creation")
    rhombus = Rhombus(5, 60)
    assert rhombus.side_a == 5
    assert rhombus.angle_a == 60
    assert rhombus.angle_b == 120
    logger.info("Rhombus creation test passed")

def test_rhombus_invalid_side_length():
    logger.info("Testing Rhombus creation with invalid side length")
    with pytest.raises(ValueError):
        Rhombus(0, 60)
    logger.info("Rhombus creation with invalid side length test passed")

def test_rhombus_str_representation():
    logger.info("Testing Rhombus string representation")
    rhombus = Rhombus(5, 60)
    assert str(rhombus) == "Rhombus(side_a=5, angle_a=60, angle_b=120)"
    logger.info("Rhombus string representation test passed")

def test_rhombus_invalid_angle():
    logger.info("Testing Rhombus creation with invalid angle")
    with pytest.raises(ValueError):
        Rhombus(5, 200)
    logger.info("Rhombus creation with invalid angle test passed")