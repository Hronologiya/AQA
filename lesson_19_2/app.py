from flask import Flask, request, jsonify, send_from_directory
import os
import logging

app = Flask(__name__)

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler to log messages to a file
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Create a formatter and set the format for the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

upload_directory = './uploads'
if not os.path.exists(upload_directory):
    os.makedirs(upload_directory)


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        logger.error('No image provided')
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    if image.filename == '':
        logger.error('No selected file')
        return jsonify({'error': 'No selected file'}), 400

    filename = os.path.join(upload_directory, image.filename)
    image.save(filename)
    logger.info(f'Image uploaded: {filename}')

    return jsonify({'image_url': request.host_url + 'image/' + image.filename}), 201


@app.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    filepath = os.path.join(upload_directory, filename)
    if os.path.exists(filepath):
        content_type = request.headers.get('Accept', '')
        if 'image/' in content_type:
            logger.info(f'Image requested: {filename} (image)')
            return send_from_directory(upload_directory, filename)
        else:
            logger.info(f'Image requested: {filename} (text)')
            return jsonify({'image_url': request.host_url + 'image/' + filename}), 200
    else:
        logger.error(f'Image not found: {filename}')
        return jsonify({'error': 'Image not found'}), 404


@app.route('/delete/<filename>', methods=['DELETE'])
def delete_image(filename):
    filepath = os.path.join(upload_directory, filename)
    if not os.path.exists(filepath):
        logger.error(f'Image not found: {filename}')
        return jsonify({'error': 'Image not found'}), 404

    os.remove(filepath)
    logger.info(f'Image deleted: {filename}')
    return jsonify({'message': f'Image {filename} deleted'}), 200


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port, debug=True)