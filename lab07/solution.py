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
