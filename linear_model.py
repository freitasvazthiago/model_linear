import numpy as np
import tensorflow as tf
import pandas
import census_dataset

# pylint: enable=wrong-import-order

train_file = "adult.data"
test_file = "adult.test"

train_df = pandas.read_csv(train_file, header = None, names = census_dataset._CSV_COLUMNS)
test_df = pandas.read_csv(test_file, header = None, names = census_dataset._CSV_COLUMNS)

train_df.head()