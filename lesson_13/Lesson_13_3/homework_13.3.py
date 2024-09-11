import logging
from pathlib import Path
import xml.etree.ElementTree as ET

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def find_incoming_value(group_number):
    # Define the path to the XML file
    xml_file = Path('groups.xml')

    # Check if the file exists
    if not xml_file.exists():
        logger.error(f'File {xml_file} does not exist')
        return None

    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Search for the group with the specified number
    for group in root.findall('group'):
        number = group.find('number').text
        if number == str(group_number):
            incoming_value = group.find('timingExbytes/incoming').text
            logger.info(f'Incoming value for group {group_number}: {incoming_value}')
            return incoming_value

    logger.info(f'Group {group_number} not found')
    return None


# Example usage
find_incoming_value(0)
find_incoming_value(2)