import os
import requests
import tempfile
from assertpy import assert_that

class TestImageUpload:
    def test_upload_image(self):
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a temporary image file
            temp_file_path = os.path.join(temp_dir, 'image.jpg')
            with open(temp_file_path, 'wb') as temp_file:
                # Upload the image
                response = requests.post('http://127.0.0.1:8080/upload', files={'image': open(temp_file_path, 'rb')})
                assert_that(response.status_code).is_equal_to(201).described_as("Status code does not match the expected one")

    def test_retrieve_image(self):
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a temporary image file
            temp_file_path = os.path.join(temp_dir, 'image.jpg')
            with open(temp_file_path, 'wb') as temp_file:
                # Upload the image
                response = requests.post('http://127.0.0.1:8080/upload', files={'image': open(temp_file_path, 'rb')})
                image_url = response.json()['image_url']

                # Retrieve the image
                response = requests.get(f'http://127.0.0.1:8080/image/{image_url.split("/")[-1]}', headers={'Accept': 'image/jpeg'})
                assert_that(response.status_code).is_equal_to(200).described_as("Status code does not match the expected one")

    def test_delete_image(self):
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a temporary image file
            temp_file_path = os.path.join(temp_dir, 'image.jpg')
            with open(temp_file_path, 'wb') as temp_file:
                # Upload the image
                response = requests.post('http://127.0.0.1:8080/upload', files={'image': open(temp_file_path, 'rb')})
                image_url = response.json()['image_url']

                # Delete the image
                response = requests.delete(f'http://127.0.0.1:8080/delete/{image_url.split("/")[-1]}')
                assert_that(response.status_code).is_equal_to(200).described_as("Status code does not match the expected one")

    def test_delete_non_existing_image(self):
        # Try to delete a non-existing image
        response = requests.delete('http://127.0.0.1:8080/delete/non_existing_image.jpg')
        assert_that(response.status_code).is_equal_to(404).described_as("Status code does not match the expected one")