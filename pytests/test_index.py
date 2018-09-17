import pytest

from ipynb.fs.full.index import pd, wine_data_from_csv, wine_data_without_na, list_of_wine_dicts, find_top_5_rated, find_5_most_rated

def test_pd_import():
    assert pd is not None, "Remember to alias your pandas import 'as pd'"

def test_wine_data_from_csv():
    import pdb; pdb.set_trace()
    pass
