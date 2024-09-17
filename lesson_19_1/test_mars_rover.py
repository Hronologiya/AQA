
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class TestMarsRover:

    def test_photos_exist(self):
        photo1_path = os.path.join(CURRENT_DIR, 'mars_photo1.jpg')
        photo2_path = os.path.join(CURRENT_DIR, 'mars_photo2.jpg')

        assert os.path.exists(photo1_path), f"File {photo1_path} not found"
        assert os.path.exists(photo2_path), f"File {photo2_path} not found"

    def test_server_response_exists(self):
        response_path = os.path.join(CURRENT_DIR, 'server_response.json')

        assert os.path.exists(response_path), f"File {response_path} not found"