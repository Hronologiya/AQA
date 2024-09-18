import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add a file handler to write logs to a file
file_handler = logging.FileHandler('image_operations.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Upload an image to the server
image_path = 'test_image.jpg'
with open(image_path, 'rb') as f:
    response = requests.post('http://127.0.0.1:8080/upload', files={'image': f})

if response.status_code == 201:
    image_url = response.json()['image_url']
    logger.info(f'Image uploaded: {image_url}')
else:
    logger.error(f'Error uploading image: {response.text}')
    exit()  # Stop execution if the image download fails.

# Retrieve the image URL using a GET request with Accept header
response = requests.get(f'http://127.0.0.1:8080/image/{image_url.split("/")[-1]}', headers={'Accept': 'text/plain'})

if response.status_code == 200:
    logger.info(f'Image URL: {response.json()["image_url"]}')
else:
    logger.error(f'Error retrieving image URL: {response.text}')

# Delete the image from the server using a DELETE request
response = requests.delete(f'http://127.0.0.1:8080/delete/{image_url.split("/")[-1]}')

if response.status_code == 200:
    logger.info(f'Image deleted: {response.json()["message"]}')
else:
    logger.error(f'Error deleting image: {response.text}')