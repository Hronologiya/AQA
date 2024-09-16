"""
There is an open NASA API that allows you to obtain data in JSON format about photos taken by the “Curiosity”
rover on Mars based on certain parameters. Among this data, there are links to photos that need to be parsed
and then downloaded and saved as local files (mars_photo1.jpg, mars_photo2.jpg) using additional requests.
The task needs to be done using the requests module.
"""

import requests
import json


def fetch_mars_photos(sol, camera, api_key):
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': sol, 'camera': camera, 'api_key': api_key}
    response = requests.get(url, params=params)

    print("Response status:", response.status_code)
    print("Server response (JSON):", response.json())

    response.raise_for_status()

    with open('server_response.json', 'w') as f:
        json.dump(response.json(), f, indent=4)

    return response.json()['photos']


def save_photo(photo_url, file_name):
    response = requests.get(photo_url)
    response.raise_for_status()
    with open(file_name, 'wb') as file:
        file.write(response.content)


def main():
    sol = 1000
    camera = 'fhaz'
    api_key = 'DEMO_KEY'
    photos = fetch_mars_photos(sol, camera, api_key)

    for idx, photo in enumerate(photos[:2], start=1):
        file_name = f'mars_photo{idx}.jpg'
        save_photo(photo['img_src'], file_name)
        print(f'Saved {file_name}')


if __name__ == "__main__":
    main()
