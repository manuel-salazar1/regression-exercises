import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.model_selection import train_test_split




# This function will create dummy variable columns

def create_dummy_variables(df, dummy_cols):
    '''
    inputs:
    df , variable with list of strings or single string
    output:
    df with dummy columns
    '''
    dummy_df = pd.get_dummies(df[dummy_cols], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    return df


#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------


# This function will scale data with Min Max scaler

def scale_data(train,
              validate,
              test,
              to_scale):
    '''
    create to_scale variable with a list of columns you want to scale
    returns:
    train_scaled, validate_scaled, test_scaled
    '''
    # make copies for scaling
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()
    
    # Make the thing
    scaler = MinMaxScaler()
    
    #fit the thing
    scaler.fit(train[to_scale])
    
    #use the thing
    train_scaled[to_scale] = scaler.transform(train[to_scale])
    validate_scaled[to_scale] = scaler.transform(validate[to_scale])
    test_scaled[to_scale] = scaler.transform(test[to_scale])
    
    return train_scaled, validate_scaled, test_scaled



#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------




# create function to initiate X_y train, validate, test

def Xy_train_val_test(train, validate, test, target_variable, drop_cols):
    """
    input train, validate, test, after using split function()
    input target_variable as string
    drop_cols formatted as: ['col1', 'col2', 'etc'] for multiple columns
        This function will drop all 'object' columns. Identify additional 
        columns you want to drop and insert 1 column as a string or multiple
        columns in a list of strings.
    returns:
    X_train, X_validate, X_test, y_train, y_validate, y_test
    """
    
    baseline_accuracy = train[target_variable].mean()
    print(f'Baseline Accuracy: {baseline_accuracy}')
    
    X_train = train.select_dtypes(exclude=['object']).drop(columns=[target_variable]).drop(columns=drop_cols)
    X_validate = validate.select_dtypes(exclude=['object']).drop(columns=[target_variable]).drop(columns=drop_cols)
    X_test = test.select_dtypes(exclude=['object']).drop(columns=[target_variable]).drop(columns=drop_cols)
    
    y_train = train[target_variable]
    y_validate = validate[target_variable]
    y_test = test[target_variable]
    
    return X_train, X_validate, X_test, y_train, y_validate, y_test









