import pandas as pd
from datasets import Dataset, load_dataset

# Load the CSV files into pandas DataFrames
# train_data = pd.read_csv('train_dataset.csv')
# test_data = pd.read_csv('test_dataset.csv')
# val_data = pd.read_csv('validation_dataset.csv')
#
# # Convert pandas DataFrames to Hugging Face Dataset
# train_dataset = Dataset.from_pandas(train_data)
# test_dataset = Dataset.from_pandas(test_data)
# val_dataset = Dataset.from_pandas(val_data)
#
# # Optionally, you can give a name to your dataset
# train_dataset = train_dataset.rename_column("Summary", "label")
#
# # You can also set the column types if needed
# train_dataset = train_dataset.with_format("csv")
# test_dataset = test_dataset.with_format("csv")
# val_dataset = val_dataset.with_format("csv")
#
# # Print a few examples
# print(train_dataset['column_name'][:3])


dataset = load_dataset('csv', data_files={'train': 'train_dataset.csv', 'validation': 'validation_dataset.csv', 'test': 'test_dataset.csv'})

print(dataset)