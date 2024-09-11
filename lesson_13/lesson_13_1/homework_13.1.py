from pathlib import Path
import pandas as pd

directory = Path(__file__).parent

file1 = directory / 'random.csv'
file2 = directory / 'random-michaels.csv'

data1 = pd.read_csv(file1)
data2 = pd.read_csv(file2)

combined_data = pd.concat([data1, data2]). drop_duplicates()

output_file = directory / 'result_your_second_name.csv'
combined_data.to_csv(output_file, index=False)

print(f"Файл без дублікатів збережено як: {output_file}")