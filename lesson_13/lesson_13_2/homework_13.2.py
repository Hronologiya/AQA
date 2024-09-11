import json
import logging
from pathlib import Path


log_file = Path('json__your_second_name.log')
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

json_directory = Path('C:\\Project\\AQA\\lesson_13\\lesson_13_2')

if not json_directory.exists():
    print(f"Directory {json_directory} does not exist.")
    exit(1)

all_files = json_directory.glob('*')

for file_path in all_files:
    if file_path.is_file() and file_path.suffix == '.json':
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                json.load(file)
            print(f"{file_path.name} it's valid json.")
        except json.JSONDecodeError as e:
            logging.error(f"File {file_path.name} is not valid json: {e}")
            print(f"File {file_path.name} is not valid json. Check the log file.")
        except Exception as e:
            logging.error(f"Error with the file {file_path}: {e}")
            print(f"Error with the file {file_path.name}. Check the log file.")
    else:
        print(f"{file_path.name} is not a json file.")