##
## EPITECH PROJECT, 2021
## 309pollution
## File description:
## Pollution
##

from math import factorial, pow
from typing import List, Tuple


class Pollution:
    def __init__(self, numerical_args: list, file_content: list) -> None:
        self._n = numerical_args[0]
        self._coordinates = (numerical_args[1], numerical_args[2])
        self._city_map = [[0 for _ in range(self._n)] for _ in range(self._n)]
        self._file_content = file_content

    @property
    def fileContent(self) -> List[List[int]]:
        return self._file_content

    @property
    def cityMap(self) -> List[List[int]]:
        return self._city_map

    @property
    def chosenCoordinates(self) -> Tuple[float, float]:
        return self._coordinates

    @property
    def size(self) -> int:
        return self._n

    def fill_map(self) -> None:
        for coords in self._file_content:
            self._city_map[coords[0]][coords[1]] = coords[2]

    def get_binomial_coef(self, n: float, k: float) -> float:
        return factorial(n) / (factorial(k) * factorial(n - k))

    def compute_bezier_values(self) -> float:
        pollution_value = float(0)

        for x in range(self._n):
            for y in range(self._n):
                pollution_value += self.get_binomial_coef(self._n - 1, x) * self.get_binomial_coef(self._n - 1, y) \
                                   * pow(self._coordinates[0] / (self._n - 1), x) \
                                   * pow(1 - (self._coordinates[0] / (self._n - 1)), (self._n - 1) - x) \
                                   * pow(self._coordinates[1] / (self._n - 1), y) \
                                   * pow(1 - (self._coordinates[1] / (self._n - 1)), (self._n - 1) - y) \
                                   * self._city_map[x][y]
        return pollution_value

    def launch_engine(self) -> None:
        self.fill_map()
        print(f'{self.compute_bezier_values():.2f}')
