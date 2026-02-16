import pandas as pd
def load_data(filepath):
    try:
        df=pd.read_csv(filepath)
        print("data loaded successfully")
        return df
    except Exception as e:
        print("error loading data:",e)
        return None