from pathlib import Path

import numpy as np
from numpy import ndarray
from functools import reduce


def read_input(pth: Path) -> ndarray:
    with open(pth, 'r') as inputhandle:
        return np.array([list(line.strip()) for line in inputhandle])


if __name__ == '__main__':
    forest = read_input(Path(Path(__file__).parent / 'input_day3.txt').resolve())

    starting_forest = forest
    forest_end, forest_width = forest.shape

    tree = '#'

    slopes = zip([1, 1, 1, 1, 2], [1, 3, 5, 7, 1])

    treecounts = []
    for drow, dcol in slopes:
        assert drow >= 0
        assert dcol >= 0
        assert not (drow == 0 and dcol == 0)

        row, col = 0, 0
        ntrees = 0

        while row < forest_end:

            if forest[row, col % forest_width] == tree:
                ntrees += 1

            row += drow
            col += dcol

        print(f"We've encountered {ntrees} trees in our wander through the forest with slope Right {dcol} Down {drow}.")
        treecounts.append(ntrees)

    print(f"The multiple of encountered trees = {reduce(lambda x, y: x * y, treecounts)}")
