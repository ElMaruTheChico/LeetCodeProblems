import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    cleanCustomers = customers.drop_duplicates(subset=['email'])
    return cleanCustomers
    