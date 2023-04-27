import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

def chart(df, region, year):
    df.loc[region, year].plot(kind='pie',
                              autopct='%.3f%%',
                              startangle=10,
                              colors=['#993399','#DCDCDC'],
                              textprops={'size':15, 'color':'white', 'weight':'bold'})
    plt.legend(df['유형'])
    plt.show()

# region_input = Element("region_input")

region_input = ET.Element("region_input")
def plot1(*args):
    region = region_input
    df_ = pd.read_csv("population.csv", encoding='cp949')
    df = df_[['자치구', '유형', '2013', '2014', '2015','2016','2017', '2018', '2019', '2020', '2021']]
    df.set_index('자치구', drop=True,inplace=True)
    
    # url1 = "https://raw.githubusercontent.com/GGAM-DAL/2LEE_PROJECT/main/population.csv"
    # df = pd.read_csv(url1, encoding='cp949')
    # df.set_index('자치구', drop=True,inplace=True)
    chart(df, region, '2013')
if __name__ == '__main__':
    plot1()

