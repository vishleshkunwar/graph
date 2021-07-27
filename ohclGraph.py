import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def graph(df):
    df['Date']=pd.to_datetime(df['Date'])
    df=df[df['Date'].dt.year>2020]
    df=df.rename(columns={'Date':'d','Open Price':'o',
                        'High Price':'h',
                        'Low Price':'l',
                        'Close Price':'c'})
    x=np.arange(0,len(df))
    fig, ax = plt.subplots(1, figsize=(12,6))
    for idx, val in df.iterrows():
        color = 'r'
        if val['c'] >= val['o']: color= 'g'
        plt.plot([x[idx], x[idx]], [val['l'], val['h']], color=color)
        plt.plot([x[idx], x[idx]-0.1], [val['o'], val['o']], color=color)
        plt.plot([x[idx], x[idx]+0.1], [val['c'], val['c']], color=color)

    # ticks
    plt.xticks(x[::20], df.d.dt.date[::20])
    ax.invert_xaxis()
    ax.yaxis.tick_right()
    # labels
    plt.xlabel('Date',color='hotpink',fontsize=10)
    ax.yaxis.set_label_position("right")
    plt.ylabel('PRICE \n(RUPEES)',color='hotpink',fontsize=10)
    # grid
    ax.xaxis.grid(color='black', linestyle='dashed', which='both', alpha=0.1)
    # remove spines
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # title
    plt.title('ACC Stock Price', loc='center', fontsize=20,color='purple')
    plt.show()