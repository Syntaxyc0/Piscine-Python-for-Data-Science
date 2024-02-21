from typing import Any
import sys

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    numbers = list(args)
    num_elems = len(numbers)
    results = dict()
    sorted = [arg for arg in args]
    if (num_elems == 0):
        for i in range(len(kwargs)):
            print("ERROR")
        sys.exit(1)
    try:
        for elem in numbers:
            int(elem)
    except:
        print("ERROR")
        sys.exit(1)
    mean = sum(numbers) * 1.0 / num_elems
    results["mean"] = mean
    for i in range(num_elems):
        for j in range(num_elems - 1):
            if (sorted[j] > sorted[j + 1]):
                sorted[j], sorted[j + 1] = sorted[j + 1], sorted[j]
        j = 0
    index = num_elems // 2
    if (num_elems % 2 == 0):
        median = (sorted[index - 1] + sorted[index]) / 2.0
    else:
        median = float(sorted[index])
    results['median'] = median
    index = num_elems // 4
    if (num_elems % 4 == 0):
        first = (sorted[index - 1] + sorted[index]) / 2.0
    else:
        first = float(sorted[index])
    index *= 3
    if (num_elems % 4 == 0):
        print(sorted[index - 1])
        print(sorted[index ])
        third = (sorted[index - 1] + sorted[index]) / 2.0
    else:
        third = float(sorted[index])
    quartile = [first, third]
    results['quartile'] = quartile
    var = 0
    for elem in numbers:
        var += (elem - mean) ** 2
    var /= num_elems
    results['var'] = var
    std = var ** 0.5
    results['std'] = std
    for key, value in kwargs.items():
        if value in results:
            print(f"{value} : {results[value]}")
        
                 
            