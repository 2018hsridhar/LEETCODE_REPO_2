'''
2887. Fill Missing Data
Crucial to fill in missing values ( handle dataset bias ) 
Considered as a form of imputation
Easier to deal with standardized vs non-standardized data
Name Error : null vs None WTF

fillna(...) null handling it seems?
'''
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # products.replace(to_replace='None', value='0', inplace=True)
    # products.replace(None, 0)
    # this is a series ( columnar ) replacement : careful!
    # products["price"].fillna(0,inplace=True)
    # print(products)
    products["quantity"].fillna(0,inplace=True)
    # print(products)
    return products
    
