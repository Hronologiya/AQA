import os
import csv
import pytest

def full_path(filename):
    """Returns the full path to the file."""
    return os.path.join(os.path.dirname(__file__), filename)

class TestCSVColumnCount:
    """Test class for checking the number of columns in a CSV file."""

    def test_column_count(self):
        """Test to check the number of columns in the CSV file."""
        data_file_path = full_path('randominfo/data.csv')  # Adjust the path if needed

        # Check if the file exists
        assert os.path.isfile(data_file_path), f"File not found: {data_file_path}"

        with open(data_file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                # Check if the row has at least 10 columns
                assert len(row) >= 10, f"Insufficient number of columns in row {index + 1}: {row}"
