import pandas as pd
import math
from data.day3data import datastring

def buildframe(slope: tuple, datastring: str) -> pd.DataFrame:
    """
    slope = x, y
    shape = y, x
    :param slope:
    :type slope:
    :param datasstring:
    :type datasstring:
    :return:
    :rtype:
    """
    rows = pd.DataFrame([[x for x in c] for c in datastring.split("\n")])
    shape = rows.shape
    # frame y never changes we only add to frame x
    # frame y / slope y * slope x
    xneeded = (shape[0] / slope[1]) * slope[0]
    framecount = int(xneeded // shape[1] + 1)

    return pd.concat([rows] * framecount, axis=1, sort=False)


def get_series(slope, nrows):
    y_index = 0
    x_index = 0
    series = []
    while y_index < nrows.shape[0]:
        series.append(nrows.iat[y_index, x_index])
        y_index += slope[1]
        x_index += slope[0]
    return series

def answer1(datastring, slope, target):
    nrows = buildframe(slope, datastring)
    return len([c for c in get_series(slope, nrows) if c == target])


print(answer1(
    datastring,
    (3, 1),
    "#"))

def answer2(slopes, datastring, target):

    counts = [answer1(datastring, slope, target) for slope in slopes]
    return math.prod(counts)

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)]

a2 = answer2(slopes, datastring, "#")
print(a2)