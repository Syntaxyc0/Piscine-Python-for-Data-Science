import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from load_csv import load

def computeTicks (country1, country2):
    if (max(country1) > max(country2)):
        x = country1
    else:
        x = country2
    xMax, xMin = math.ceil(max(x)), math.floor(min(x))
    step = int((xMax - xMin) / 5)
    dMax, dMin = xMax + abs((xMax % step) - step) + (step if (xMax % step != 0) else 0), xMin - abs((xMin % step))
    res = [int(math.ceil(i / 10.0)) * 10 for i in range(dMin, dMax, step)]
    return res
        

def convert_population_to_millions(population):
    population = population.replace('M', '')
    population = population.replace('B', 'E3')
    return float(population)


def main():
    table = load("population_total.csv")
    table.set_index("country", inplace = True)
    China = table.loc['China'][0:252]
    India = table.loc['India'][0:252]
    China = China.map(convert_population_to_millions).to_numpy()
    India = India.map(convert_population_to_millions).to_numpy()
    years = table.columns[0:252].to_numpy()
    plt.figure(figsize=(10,6))
    plt.yticks(computeTicks(India, China))
    plt.plot(years, India, label='India')
    plt.plot(years, China, label='China')
    plt.xlabel('Year')
    plt.xticks(["1800", "1840", "1880", "1920", "1960", "2000", "2040"])
    plt.ylabel('Population (in millions)')
    plt.title("Population Projections")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
