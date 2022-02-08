##
## EPITECH PROJECT, 2021
## 309pollution
## File description:
## ArgChecker
##

from os.path import exists, splitext
from typing import List, Union
import csv


class ArgumentException(Exception):
    def __init__(self, message="Error occurs when handling an argument!"):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class ArgChecker:
    def __init__(self) -> None:
        self._cleaned_args = list()
        self._file_content = list()
        pass

    @property
    def numericalArgs(self) -> List[Union[int, float]]:
        return self._cleaned_args

    @property
    def fileContent(self) -> List[str]:
        return self._file_content

    def are_numerical_args_conform(self, args: list) -> bool:
        index = int(0)

        for tmp in args:
            try:
                value = int(tmp) if index == 0 else float(tmp)
                self._cleaned_args.append(value)
                index += 1
            except ValueError as err:
                self._cleaned_args = None
                print(f"{type(err).__name__}: {err}")
                return False
        if any(value < 0 for value in self._cleaned_args):
            return False
        return True

    def is_file_conform(self, filepath: str) -> bool:
        if not exists(filepath):
            return False
        with open(filepath, encoding="utf-8") as fd:
            reader = csv.reader(fd, delimiter=';')
            try:
                for row in reader:
                    if len(row) != 3:
                        raise ArgumentException("CSV File must have only 3 variables per line")
                    _ = [int(value) for value in row]
                    if any(value < 0 for value in _):
                        raise ArgumentException("CSV File must contain only positive coordinates.")
                    elif _[0] >= self._cleaned_args[0] or _[1] >= self._cleaned_args[0]:
                        raise ArgumentException("CSV File must contain coordinates between 0 and 'n' argument.")
                    self._file_content.append(_)
            except ValueError as err:
                self._file_content = None
                print(f"{type(err).__name__}: {err}")
                return False
            except ArgumentException as err:
                self._file_content = None
                print(f"{type(err).__name__}: {err}")
                return False
        fd.close()
        return True

    def check_args_conformity(self, args: list) -> bool:
        if not self.are_numerical_args_conform(args[:1] + args[2:]) or not self.is_file_conform(args[1]):
            return False
        return True
