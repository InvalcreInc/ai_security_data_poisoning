import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join('..')))


def load_dataset(filename):
    """
    Load the dataset from the 'data' folder.
    """
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(script_dir)
    dataset_dir = os.path.join(parent_dir, 'data')
    filepath = os.path.join(dataset_dir, filename)
    return pd.read_csv(filepath)
