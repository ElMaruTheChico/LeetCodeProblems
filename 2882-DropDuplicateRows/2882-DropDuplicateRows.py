import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    cleandf = students.dropna(subset=['name'])
    return cleandf
    