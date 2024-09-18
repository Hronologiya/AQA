import os
import requests
import tempfile

def test_upload_retrieve_image():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a temporary image file
        temp_file_path = os.path.join(temp_dir, 'image.jpg')
        with open(temp_file_path, 'wb') as temp_file:
            # Upload the image
            response = requests.post('http://127.0.0.1:8080/upload', files={'image': open(temp_file_path, 'rb')})
            assert response.status_code == 201
            image_url = response.json()['image_url']

            # Retrieve the image
            response = requests.get(f'http://127.0.0.1:8080/image/{image_url.split("/")[-1]}', headers={'Accept': 'image/jpeg'})
            assert response.status_code == 200

            # Save the retrieved image to a temporary file
            temp_file_path2 = os.path.join(temp_dir, 'image2.jpg')
            with open(temp_file_path2, 'wb') as temp_file2:
                temp_file2.write(response.content)

            # Verify that the uploaded and retrieved images are the same
            with open(temp_file_path, 'rb') as f1, open(temp_file_path2, 'rb') as f2:
                assert f1.read() == f2.read()

        # Delete the image
        response = requests.delete(f'http://127.0.0.1:8080/delete/{image_url.split("/")[-1]}')
        assert response.status_code == 200

def test_delete_non_existing_image():
    # Try to delete a non-existing image
    response = requests.delete('http://127.0.0.1:8080/delete/non_existing_image.jpg')
    assert response.status_code == 404