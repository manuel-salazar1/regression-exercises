#Imports

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.model_selection import train_test_split



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
    # rename fips to county
    df = df.rename(columns={'fips': 'county'})
    
    #drop all nulls
    df = df.dropna()
    
    # making list to change dtype to integers
    make_ints = ['bedrooms', 'sqft', 'tax_value', 'year_built']

    for col in make_ints:
        df[col] = df[col].astype(int)

    # giving couty names instead of numbers    
    df.county = df.county.map({6037:'la', 6059:'orange', 6111:'ventura'})
    
    # Create dummy variables for the county column
    dummy_df = pd.get_dummies(df['county'], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)

    # dropping outliers
    df = df[df.bedrooms.between(1,7)]
    df = df[df.bathrooms.between(1,6)]
    df = df[df.sqft <= df.sqft.mean() + (4 * df.sqft.std())]
    df = df[df.sqft >= 500]
    df = df [df.tax_value < df.tax_value.quantile(.95)]
    
    return df




#SPLIT FUNCTION

def split_function(df):
    '''
    Take in a data frame and returns train, validate, test subset data frames
    '''
    train, test = train_test_split(df,
                              test_size=0.20,
                              random_state=123,
                                  )
    train, validate = train_test_split(train,
                                  test_size=.25,
                                  random_state=123,
                                      )
    return train, validate, test






