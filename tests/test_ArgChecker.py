##
## EPITECH PROJECT, 2021
## 309pollution
## File description:
## test_ArgChecker
##

from sources.ArgChecker import ArgChecker


class TestArgChecker:
    def test_basic_args(self) -> None:
        tArgChecker = ArgChecker()
        assert tArgChecker.are_numerical_args_conform(['3', '0', '2'])

    def test_float_second_args(self) -> None:
        tArgChecker = ArgChecker()
        assert tArgChecker.are_numerical_args_conform(['3', '0.5', '2'])

    def test_all_checks_args(self) -> None:
        tArgChecker = ArgChecker()
        assert tArgChecker.check_args_conformity(['3', './test_files/test.csv', '0', '2'])

    def test_wrong_checks_args(self) -> None:
        tArgChecker = ArgChecker()
        assert not tArgChecker.check_args_conformity(['3', './test_files/wrong_test.csv', '0.5', '2'])

    def test_wrong_type_arg(self, capsys) -> None:
        tArgChecker = ArgChecker()
        assert not tArgChecker.are_numerical_args_conform(['3.12', '0', '2'])
        stdout = capsys.readouterr()[0]
        assert stdout == "ValueError: invalid literal for int() with base 10: '3.12'\n"
        assert tArgChecker.numericalArgs is None

    def test_basic_file(self) -> None:
        tArgChecker = ArgChecker()
        if tArgChecker.are_numerical_args_conform(["3", "0", "2"]):
            assert tArgChecker.is_file_conform('./test_files/test.csv')

    def test_file_with_wrong_values(self, capsys) -> None:
        tArgChecker = ArgChecker()
        if tArgChecker.are_numerical_args_conform(["3", "0", "2"]):
            assert not tArgChecker.is_file_conform('./test_files/wrong_test.csv')
            stdout = capsys.readouterr()[0]
            assert stdout == "ValueError: invalid literal for int() with base 10: 'a'\n"
            assert tArgChecker.fileContent is None

    def test_file_with_negative_arguments(self) -> None:
        tArgChecker = ArgChecker()
        assert not tArgChecker.are_numerical_args_conform(["-3", "0", "-2"])

    def test_file_with_negative_coordinates(self) -> None:
        tArgChecker = ArgChecker()
        if tArgChecker.are_numerical_args_conform(["3", "0", "2"]):
            assert not tArgChecker.is_file_conform('./test_files/negative_coordinates_file.csv')

    def test_file_with_higher_coordinates_than_size(self) -> None:
        tArgChecker = ArgChecker()
        if tArgChecker.are_numerical_args_conform(["3", "0", "2"]):
            assert not tArgChecker.is_file_conform('./test_files/higher_than_size.csv')

    def test_wrong_coordinates_in_file(self) -> None:
        tArgChecker = ArgChecker()
        if tArgChecker.are_numerical_args_conform(["3", "0", "2"]):
            assert not tArgChecker.is_file_conform('./test_files/wrong_test_2.csv')

    def test_maybe_a_wrong_file(self) -> None:
        tArgChecker = ArgChecker()
        assert not tArgChecker.is_file_conform("./test_files/maybe_a_wrong_file.txt")

    def test_unknown_file(self) -> None:
        tArgChecker = ArgChecker()
        assert not tArgChecker.is_file_conform("unknown_file.csv")
