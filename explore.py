#Imports

import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.model_selection import train_test_split

import wrangle




def plot_variable_pairs(train):
    '''
    Insert train dataframe
    This function is taking a sample of 100_000 to speed the process up
    '''
    # isolating columns I want to plot with target variable
    columns_to_plot = ['bedrooms', 'bathrooms', 'sqft', 'year_built', 'tax_amount']
    
    # created a for loop to plot variable with target variable including regression line
    for col in columns_to_plot:
        sns.regplot(x=col, y='tax_value', data=train.sample(100_000), line_kws = {'color':'red'})
        plt.title(f'{col} vs. tax value')
        plt.show()








def plot_categorical_and_continuous_vars(train, cont, cat):
    '''
    input cont and cat variables as strings
    i.e. 'bedrooms', 'sqft'
    '''
    cont_var= cont
    cat_var = cat
    
    # create a figure with 2 rows and 3 columns of subplots
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))
    
    # plot data on each subplot
    sns.jointplot(x=cont_var, y='tax_value', data=train.sample(100_000), kind='scatter', ax=axes[0, 0])
    sns.regplot(x=cont_var, y='tax_value', data=train.sample(100_000), line_kws = {'color':'red'}, ax=axes[0, 1])
    sns.scatterplot(x=cont_var, y='tax_value', data=train.sample(100_000), ax=axes[0, 2])
    
    sns.barplot(x=cat_var, y='tax_value', data=train.sample(100_000), ax=axes[1, 0])
    sns.violinplot(x=cat_var, y='tax_value', data=train.sample(100_000), ax=axes[1, 1])
    sns.boxplot(x=cat_var, y='tax_value', data=train.sample(100_000), ax=axes[1, 2])
    
    plt.tight_layout()
    plt.show()






















