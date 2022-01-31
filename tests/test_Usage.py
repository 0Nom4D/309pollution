##
## EPITECH PROJECT, 2021
## 309pollution
## File description:
## test_Usage
##

from sources.main import print_usage


usage_results = "USAGE\n\t./309pollution n file x y\n"\
          "DESCRIPTION\n"\
          "\tn\tnumber of points on the grid axis\n"\
          "\tfile\tcsv file containing the data points x;y;p\n"\
          "\tx\tabscissa of the point whose pollution level we want to know\n"\
          "\ty\tordinate of the point whose pollution level we want to know\n"

def test_usage_print(capsys):
    print_usage()
    stdout = capsys.readouterr()[0]
    assert stdout == usage_results
