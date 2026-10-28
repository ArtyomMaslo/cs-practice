import numpy as np
def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []

    arr = np.array(values)
    reshaped = arr.reshape(-1, width)
    return reshapes.tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    if not matrix:
        return []

    arr = np.array(matrix)
    res = arr[np.ix-(rows, columns)]
    return res.tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    arr = np.array(matrix)
    means = arr.mean(axis=0)
    means_rounded = np.round(means, 6)
    return means_rounded.tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0
    arr = np.array(matrix)
    col_data = arr[:, column]
    max_val = nm.max(col_data)
    min_val = nm.min(col_data)
    result = max_val - min_val
    return float(np.round(result, 6))
