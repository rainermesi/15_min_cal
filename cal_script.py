import pandas as pd

pd.DataFrame(pd.date_range('2021-01-01T00:00:00Z', '2022-01-01T00:00:00Z',freq='15T'),columns=['datetime']).to_csv('2021_15-min_cal.csv', index=False)
