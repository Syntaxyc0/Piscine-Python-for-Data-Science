import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def main():
    table = load("population_total.csv")
    years = table.columns[0:252]
    table.set_index("country", inplace = True)
    france = table.loc['France'][0:252]
    Pakistan = table.loc['Pakistan'][0:252]
    plt.figure(figsize=(10,6))
    plt.plot(years, france, label='France')
    plt.plot(years, Pakistan, label='Pakistan')
    plt.xlabel('Year')
    plt.xticks(["1800", "1840", "1880", "1920", "1960", "2000", "2040"], rotation=0)
    plt.ylabel('Population')
    plt.title("Population Projections")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
