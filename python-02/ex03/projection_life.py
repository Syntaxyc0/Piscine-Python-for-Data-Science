import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from load_csv import load


def main():
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv").loc[:, '1900']
    life_expectancy = load("life_expectancy_years.csv").loc[:, '1900']
    print(income)
    print(life_expectancy)
    plt.scatter(income, life_expectancy)
    plt.xscale('log')
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life Expectancy')
    plt.title('1900')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.show()
 

if __name__ == '__main__':
    main()
