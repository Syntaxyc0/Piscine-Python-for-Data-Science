import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def main():
    table = load("life_expectancy_years.csv")
    table.set_index("country", inplace = True)
    table = table.loc['France']
    plt.plot(table)
    plt.xlabel('Year')
    plt.xticks(["1800", "1840", "1880", "1920", "1960", "2000", "2040", "2080"], rotation=0)
    plt.ylabel('Life expectancy')
    plt.title("France Life expectancy Projections")
    plt.show()


if __name__ == '__main__':
    main()
