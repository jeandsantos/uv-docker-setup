import pandas as pd

from uv_setup.data import generate_data


class TestGenerateData:
    def test_generate_data(self):
        result = generate_data()

        assert isinstance(result, pd.DataFrame), "Result should be a DataFrame"
        assert len(result) == 5, "DataFrame should have 5 rows"
