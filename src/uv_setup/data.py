import pandas as pd


def generate_data():
    """
    Generates a sample DataFrame with random data for demonstration purposes.

    Returns:
        pd.DataFrame: A DataFrame containing random data.
    """
    data = {"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1], "C": ["a", "b", "c", "d", "e"]}
    df = pd.DataFrame(data)
    return df
