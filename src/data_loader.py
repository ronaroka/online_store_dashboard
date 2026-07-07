import pandas as pd

def load_data(source):

    if hasattr(source, "name"):
        # uploaded file
        if source.name.endswith(".csv"):
            return pd.read_csv(source)
        elif source.name.endswith(".xlsx"):
            return pd.read_excel(source)

    else:
        # URL
        if source.endswith(".csv"):
            return pd.read_csv(source)
        else:
            return pd.read_excel(source)