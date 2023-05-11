# Regression functions


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_residuals(y, yhat):
    '''
    send in: 
    i.e. y = train.tax_value
      yhat = train.yhat
    '''
    
    residuals = y - yhat
    sns.scatterplot(y=residuals, x=y, hue=y, size=y)
    
    baseline = y.mean()
    plt.axhline(baseline, ls=':', color='red')
    
    plt.xlabel('Actual')
    plt.ylabel('Residual')
    plt.title('Residual Plot')
    plt.show()



def regression_errors(y, yhat):
    '''
    send in: 
    i.e.
    y = train.tax_value
    yhat = train.yhat
    return:
    SSE, ESS, TSS, MSE, RMSE
    '''
    MSE = mean_squared_error(y, yhat)
    SSE = MSE * len(y)
    RMSE = MSE ** .5
    
    ESS = ((yhat - y.mean()) ** 2).sum()
    TSS = ESS + SSE
    
    
    
    print(f'Metric  Model_error')
    print(f'SSE:   ', SSE)
    print(f'ESS:   ', ESS)
    print(f'TSS:   ', TSS)
    print(f'MSE:   ', MSE)
    print(f'RMSE:  ', RMSE)
    
    return SSE, ESS, TSS, MSE, RMSE



def baseline_mean_errors(y):
    '''
    send in: 
    df
    y = target variable as string
    You NEED to have a baseline column in df for this function to work
    return SSE_baseline, MSE_baseline, RMSE_baseline
    '''
    
    baseline = np.repeat(y.mean(), len(y))
    MSE_baseline = mean_squared_error(y, baseline)
    SSE_baseline = MSE_baseline * len(y)
    RMSE_baseline = MSE_baseline ** .5
    
    
    print(f'                 error')
    print(f'SSE Baseline: ', sse_baseline)
    print(f'MSE baseline: ', mse_baseline)
    print(f'RMSE Baseline:', rmse_baseline)
    
    return SSE_baseline, MSE_baseline, RMSE_baseline




def better_than_baseline(y, yhat, baseline):
    '''
    ex: train.tax_value for y
    train.yhat for yhat
    train.baseline for baseline
    '''
    sse_model = np.sum((y - yhat) ** 2)
    sse_baseline = np.sum((y - baseline) ** 2)

    return sse_model < sse_baseline






