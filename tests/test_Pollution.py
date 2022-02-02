##
## EPITECH PROJECT, 2021
## 309pollution
## File description:
## test_Pollution
##

from sources.ArgChecker import ArgChecker
from sources.Pollution import Pollution


class TestPollutionEngine:
    def test_pollution_engine_creation(self) -> None:
        tArgChecker = ArgChecker()
        if tArgChecker.check_args_conformity(["3", "./test_files/test.csv", "0", "2"]):
            tPolluter = Pollution(tArgChecker.numericalArgs, tArgChecker.fileContent)
            assert tPolluter.size == 3
            assert tPolluter.chosenCoordinates == (0, 2)
            assert tPolluter.cityMap == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            assert tPolluter.fileContent == [[0, 0, 20], [0, 1, 12], [1, 0, 50], [1, 1, 30], [1, 2, 50], [2, 2, 80]]

    def test_map_filling(self) -> None:
        tArgChecker = ArgChecker()
        if tArgChecker.check_args_conformity(["3", "./test_files/test.csv", "0", "2"]):
            tPolluter = Pollution(tArgChecker.numericalArgs, tArgChecker.fileContent)
            tPolluter.fill_map()
            assert not tPolluter.cityMap == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_beziers_values_computation(self) -> None:
        tArgChecker = ArgChecker()
        if tArgChecker.check_args_conformity(["3", "./test_files/test.csv", "0.8", "0.8"]):
            tPolluter = Pollution(tArgChecker.numericalArgs, tArgChecker.fileContent)
            tPolluter.fill_map()
            assert tPolluter.compute_bezier_values() == 26.1056
