import pytest

from ipynb.fs.full.index import pd, wine_data_from_csv, wine_data_without_na, list_of_wine_dicts, find_top_5_rated, find_5_most_rated

def test_pd_import():
    assert pd is not None

def test_wine_data_from_csv():
    assert type(wine_data_from_csv) == type(pd.DataFrame())
    assert len(wine_data_from_csv) == 560

def test_wine_data_without_na():
    assert type(wine_data_without_na) == type(pd.DataFrame())
    assert len(wine_data_without_na) == 560
    assert not wine_data_without_na.isnull().any().any()

def test_list_of_wine_dicts():
    assert type(list_of_wine_dicts) == type([])
    assert type(list_of_wine_dicts[0]) == type({})
    assert len(list_of_wine_dicts) == 560

def test_find_top_5_rated():
    assert type(find_top_5_rated(list_of_wine_dicts)) == type([])
    assert len(find_top_5_rated(list_of_wine_dicts)) == 5
    assert find_top_5_rated(list_of_wine_dicts) == top_5_rated()

def test_find_5_most_rated():
    assert type(find_5_most_rated(list_of_wine_dicts)) == type([])
    assert len(find_5_most_rated(list_of_wine_dicts)) == 5
    assert find_5_most_rated(list_of_wine_dicts) == top_5_reviewed()

def top_5_rated():
    return  [{'Name': "Abbott's & Delaunay Fruits Sauvage Sauvignon Blanc 2017", 'num_ratings': 0, 'positive_rating': 0, 'price': 9.99, 'wine_type': 'white wine', 'country': 0, 'world': 0, 'grape': 0, 'region': 0, 'rating_score': 0.0}, {'Name': 'Aresti Bellavista Sauvignon Gris 2017', 'num_ratings': 1, 'positive_rating': 0, 'price': 10.99, 'wine_type': 'white wine', 'country': 0, 'world': 0, 'grape': 0, 'region': 0, 'rating_score': 0.0}, {'Name': 'Beringer Knights Valley Napa Cabernet 2015', 'num_ratings': 0, 'positive_rating': 0, 'price': 30.0, 'wine_type': 'red wine', 'country': 0, 'world': 0, 'grape': 0, 'region': 0, 'rating_score': 0.0}, {'Name': 'Capo Martino 2012 Jermann', 'num_ratings': 0, 'positive_rating': 0, 'price': 50.0, 'wine_type': 'fine wine', 'country': 'italian', 'world': 'old world', 'grape': 0, 'region': 0, 'rating_score': 0.0}, {'Name': 'Ch. Clos de Vaulicheres Chablis 1er Cru Vaucoupin 2015', 'num_ratings': 0, 'positive_rating': 0, 'price': 27.99, 'wine_type': 'fine wine', 'country': 0, 'world': 0, 'grape': 0, 'region': 'chablis', 'rating_score': 0.0}]

def top_5_reviewed():
  return [{'Name': "Abbott's & Delaunay Fruits Sauvage Sauvignon Blanc 2017", 'num_ratings': 0, 'positive_rating': 0, 'price': 9.99, 'wine_type': 'white wine', 'country': 0, 'world': 0, 'grape': 0, 'region': 0, 'rating_score': 0.0}, {'Name': 'Beringer Knights Valley Napa Cabernet 2015', 'num_ratings': 0, 'positive_rating': 0, 'price': 30.0, 'wine_type': 'red wine', 'country': 0, 'world': 0, 'grape': 0, 'region': 0, 'rating_score': 0.0}, {'Name': 'Capo Martino 2012 Jermann', 'num_ratings': 0, 'positive_rating': 0, 'price': 50.0, 'wine_type': 'fine wine', 'country': 'italian', 'world': 'old world', 'grape': 0, 'region': 0, 'rating_score': 0.0}, {'Name': 'Ch. Clos de Vaulicheres Chablis 1er Cru Vaucoupin 2015', 'num_ratings': 0, 'positive_rating': 0, 'price': 27.99, 'wine_type': 'fine wine', 'country': 0, 'world': 0, 'grape': 0, 'region': 'chablis', 'rating_score': 0.0}, {'Name': 'Chablis Grand Acacia J. Moreau & Fils', 'num_ratings': 0, 'positive_rating': 0, 'price': 18.99, 'wine_type': 'white wine', 'country': 'french', 'world': 'old world', 'grape': 0, 'region': 'burgundy', 'rating_score': 0.0}]
