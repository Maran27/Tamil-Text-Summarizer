import pandas as pd
from sklearn.model_selection import train_test_split

# Load the CSV file into a pandas DataFrame
csv_file_path = 'Tamil wiki-data summarized.csv'
data = pd.read_csv(csv_file_path)

# Split the data into training, testing, and validation sets
train_data, temp_data = train_test_split(data, test_size=0.3, random_state=42)
test_data, val_data = train_test_split(temp_data, test_size=0.5, random_state=42)

# Save the split datasets to new CSV files
train_data.to_csv('train_dataset.csv', index=False)
test_data.to_csv('test_dataset.csv', index=False)
val_data.to_csv('validation_dataset.csv', index=False)
