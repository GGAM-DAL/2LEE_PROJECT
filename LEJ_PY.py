import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from xml.etree.ElementTree import Element



def chart(df, region, year):
    df.loc[region, year].plot(kind='pie',
                              autopct='%.3f%%',
                              startangle=10,
                              colors=['#993399','#DCDCDC'],
                              textprops={'size':15, 'color':'white', 'weight':'bold'})
    # result.element = plt.show()

def plot1(*args):
    region = document.getElementById("region_input").value
    result = Element("result")


    result.element.innerText = print(f'선택한 지역은 {region}')
    region_input.clear()
    # url1 = "https://raw.githubusercontent.com/GGAM-DAL/2LEE_PROJECT/main/population.csv"
    # df = pd.read_csv(url1, encoding='cp949')
    # df.set_index('자치구', drop=True,inplace=True)


if __name__ == '__main__':
    plot1()

    