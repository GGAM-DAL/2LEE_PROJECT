import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def chart(df, region, year):
    df.loc[region, year].plot(kind='pie',
                              autopct='%.3f%%',
                              startangle=10,
                              colors=['#993399','#DCDCDC'],
                              textprops={'size':15, 'color':'white', 'weight':'bold'})
    plt.legend(df['유형'])
    plt.show()

# region_input = Element("region_input")
region_input = Element(region_input)
def plot1(*args):
    region = region_input.value
    df_ = pd.read_csv("population.csv", encoding='cp949')
    df = df_[['자치구', '유형', '2013', '2014', '2015','2016','2017', '2018', '2019', '2020', '2021']]
    df.set_index('자치구', drop=True,inplace=True)
    chart(df, region, '2013')
    

if __name__ == '__main__':
    plot1()

    