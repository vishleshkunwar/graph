from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from matplotlib.collections import LineCollection, PolyCollection
from matplotlib.lines import TICKLEFT, TICKRIGHT, Line2D
from matplotlib.patches import Rectangle
from matplotlib.transforms import Affine2D
from six.moves import xrange, zip

class graph:
    df = ""
    def __init__(self , type_ ,indicators,volume):
        self.type_ = type_
        self.indicators = indicators
        self.volume = volume
        self.getData()
        self.drawGraph()
    def getData(self):
        self.df =pd.read_csv('C:/Users/91766/Desktop/Stock Analysis/graph/ACC.csv')
        self.df['Date']=pd.to_datetime(self.df['Date'])
        self.df=self.df.head(50)
        self.df=self.df.rename(columns={'Date':'d','Open Price':'o',
                            'High Price':'h',
                            'Low Price':'l',
                            'Close Price':'c'})
    def drawGraph(self):
        if(self.type_=="candlestick"):
            self.candlestick()
        elif(self.type_=="heikinashi"):
            print("heikin ashi")
    def candlestick(self):
        x=np.arange(0,len(self.df))
        fig, ax = plt.subplots(1, figsize=(12,8))
        lines = []
        patches = []

        for i in x:
            if self.df['c'][i] >=self.df['o'][i]:
                color = 'g'
                lower = self.df['o'][i]
                height = self.df['c'][i] - self.df['o'][i]
            else:
                color = 'r'
                lower = self.df['c'][i]
                height = self.df['o'][i] - self.df['c'][i]

            vline = Line2D(xdata=(i, i), ydata=(self.df['l'][i],self.df['h'][i]),color=color)

            rect = Rectangle(xy=(i-0.3,lower),width=0.6,height=height,facecolor=color,edgecolor='k')
            rect.set_alpha(alpha=1.0)

            lines.append(vline)
            patches.append(rect)
            ax.add_line(vline)
            ax.add_patch(rect)
            ax.autoscale_view()
        
        # ticks top plot
        ax.set_xticks(x[::2])
        ax.set_xticklabels(self.df.d.dt.date[::2])
        ax.invert_xaxis()
        ax.yaxis.tick_right()

        # labels
        ax.yaxis.set_label_position("right")
        ax.set_ylabel('Price\n (rupees)',color='k',fontsize=10)
        ax.set_xlabel('Date',color='k',fontsize=10)

        # grid
        ax.xaxis.grid(color='black', linestyle='dashed', alpha=0.3)
        ax.yaxis.grid(color='black', linestyle='dashed', alpha=0.3)
        
        # remove spines
        ax.spines['left'].set_visible(False)
        ax.spines['top'].set_visible(False)

        # title
        ax.set_title('ACC Stock Price\n', loc='center', fontsize=20)

        plt.show()