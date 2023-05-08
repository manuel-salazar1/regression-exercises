#Imports

import pandas as pd 
from env import username, password, get_db_url
import os
import seaborn as sns
import numpy as np


#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------


# Acquire Data from zillow database in MySQL from Codeup

# Creating new SQL query 
def new_zillow_data():
    """
    This function will:
    - create a connect_url to mySQL
    - return a df of the given query from the zillow db
    """
    url = get_db_url('zillow')
    SQL_query = '''
                select bedroomcnt as bedrooms, bathroomcnt as bathrooms, calculatedfinishedsquarefeet as sqft
                    , taxvaluedollarcnt as tax_value, yearbuilt as year_built, taxamount as tax_amount, fips
                from propertylandusetype
                join properties_2017 on propertylandusetype.propertylandusetypeid = properties_2017.propertylandusetypeid
                    and properties_2017.propertylandusetypeid = 261
                '''
    return pd.read_sql(SQL_query, url)



#-------------------------------------------------------------------------------------------------------------------------------------

# Creating df 

def get_zillow_data(filename="zillow.csv"):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output zillow df
    """
    if os.path.exists(filename):
        df = pd.read_csv(filename, index_col=0) 
        print('Found CSV')
        return df
    
    else:
        df = new_zillow_data()
        
        #want to save to csv
        df.to_csv(filename)
        print('Creating CSV')
        return df




#-------------------------------------------------------------------------------------------------------------------------------------




def wrangle_zillow(df):
    df = df.rename(columns={'fips': 'county'})
    
    df = df.dropna()
    
    make_ints = ['bedrooms', 'sqft', 'tax_value', 'year_built']

    for col in make_ints:
        df[col] = df[col].astype(int)
        
    df.county = df.county.map({6037:'la', 6059:'orange', 6111:'ventura'})
    
    df = df[df.bedrooms.between(1,7)]
    df = df[df.bathrooms.between(1,6)]
    df = df[df.sqft <= df.sqft.mean() + (4 * df.sqft.std())]
    df = df[df.sqft >= 500]
    df = df [df.tax_value < df.tax_value.quantile(.95)]
    
    return df






