import numpy as np

def calculate(list):

    if(len(list) < 9):
      raise ValueError("List must contain nine numbers.")

    list = np.array(list)
    matrix = list.reshape((3,3))

    mean1 = np.mean(matrix, axis=0).tolist()
    mean2 = np.mean(matrix, axis=1).tolist()
    meanFlattened = np.mean(matrix).tolist()

    var1 = np.var(matrix, axis=0).tolist()
    var2 = np.var(matrix, axis=1).tolist()
    varFlattened = np.var(matrix).tolist()

    std1 = np.std(matrix, axis=0).tolist()
    std2 = np.std(matrix, axis=1).tolist()
    stdFlattened = np.std(matrix).tolist()

    max1 = np.max(matrix, axis=0).tolist()
    max2 = np.max(matrix, axis=1).tolist()
    maxFlattened = np.max(matrix).tolist()

    min1 = np.min(matrix, axis=0).tolist()
    min2 = np.min(matrix, axis=1).tolist()
    minFlattened = np.min(matrix).tolist()

    sum1 = np.sum(matrix, axis=0).tolist()
    sum2 = np.sum(matrix, axis=1).tolist()
    sumFlattened = np.sum(matrix).tolist()

    calculations = {
      "mean": [mean1, mean2, meanFlattened],
      "variance": [var1, var2, varFlattened],
      "standard deviation": [std1, std2, stdFlattened],
      "max": [max1, max2, maxFlattened],
      "min": [min1, min2, minFlattened],
      "sum": [sum1, sum2, sumFlattened]
    }

    return calculations
