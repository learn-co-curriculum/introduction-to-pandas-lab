import pandas as pd

csv = pd.read_csv('majestic_wine_data.csv').fillna(False)
wine_data = csv.to_dict('records')

filtered_data = [data for data in wine_data if all(data.values())]
import pdb; pdb.set_trace()
