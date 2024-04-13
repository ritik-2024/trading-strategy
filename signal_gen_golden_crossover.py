# Golden Crossover
# if 20 SMA cross to 50 SMA then we get buy signal and when 50 SMA cross 20 SMA we get sell signal

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from tabulate import tabulate

def Golden_Crossover(stack_name,dataPoint):
    
    data = pd.read_csv(f'Data/{stack_name}.csv',parse_dates=["Date"],index_col="Date")



    # print(data)

    # plot graph
    # data.plot()
    # data[-400:].Close.plot(figsize=(15,8))
    # plt.show()


    data['20_SMA']= data.Close.rolling(window=20,min_periods=1).mean()
    print(data['20_SMA'])
    data['50_SMA']= data.Close.rolling(window=50,min_periods=1).mean()
    print(data['50_SMA'])

    data['Signal']=0
    data['Signal']= np.where(data['20_SMA'] > data['50_SMA'], 1 ,0)
    print(data['Signal'])

    data['Position']= data.Signal.diff()
    print(data['Position'])

    # Golden Crossover
    # if 20 SMA cross to 50 SMA then we get buy signal and when 50 SMA cross 20 SMA we get sell signal

    plt.figure(figsize=(20,10))
    # plot close price, short-term and long term moving averages
    data.iloc[-dataPoint:]["Close"].plot(color = "k",label= 'Close Price')
    data.iloc[-dataPoint:]['20_SMA'].plot(color = "b",label= '20-day SMA')
    data.iloc[-dataPoint:]['50_SMA'].plot(color = "g",label= '50-day SMA')

    # plot 'buy' signals
    plt.plot(data.iloc[-dataPoint:][data.iloc[-dataPoint:]['Position']== 1].index,
            data.iloc[-dataPoint:]['20_SMA'][data.iloc[-dataPoint:]['Position']==1],
            '^',markersize=15,color='g',label='buy')

    # plot 'sell' signal
    plt.plot(data.iloc[-dataPoint:][data.iloc[-dataPoint:]['Position']== -1].index,
            data.iloc[-dataPoint:]['20_SMA'][data.iloc[-dataPoint:]['Position']==-1],
            'v',markersize=15,color='r',label='sell')

    plt.ylabel('Price in Rupees', fontsize =15)
    plt.xlabel('Date',fontsize=15)
    plt.title(stack_name,fontsize=20)

    plt.legend()
    plt.grid()
    plt.show()

    df_pos=data.iloc[-dataPoint:][(data.iloc[-dataPoint:]['Position']== 1) | (data['Position'] ==-1)].copy()
    df_pos['Position']= df_pos['Position'].apply(lambda x:'Buy' if x == 1 else 'sell')

    print(tabulate(df_pos[['Close','Position']],headers='keys',tablefmt='psql'))
    
Golden_Crossover('RELIANCE',300)