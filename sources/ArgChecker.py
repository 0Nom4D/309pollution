##
## EPITECH PROJECT, 2021
## 309pollution
## File description:
## ArgChecker
##

from os.path import exists, splitext
from typing import List, Union
import csv


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
        print(self.numericalArgs)
        return True

    def is_file_conform(self, filepath: str) -> bool:
        if not exists(filepath) or splitext(filepath)[1] != '.csv':
            return False
        with open(filepath, encoding="utf-8") as fd:
            reader = csv.reader(fd, delimiter=';')
            try:
                for row in reader:
                    _ = [int(value) for value in row]
                    self._file_content.append(_)
            except ValueError as err:
                self._file_content = None
                print(f"{type(err).__name__}: {err}")
                return False
        fd.close()
        return True

    def check_args_conformity(self, args: list) -> bool:
        if not self.is_file_conform(args[1]) or not self.are_numerical_args_conform(args[:1] + args[2:]):
            return False
        return True