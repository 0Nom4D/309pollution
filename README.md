# 309pollution

309pollution is a B-MAT-500 EPITECH module project.

309pollution is about monitoring ambient air quality.

## Before continuing...

This project is an EPITECH Project. If you are an EPITECH student, move out the way!

Nothing to see here... I don't want to be involved to your -42.

![Alt Text](https://media.tenor.com/images/5a5f5957db8b98be17ef208737663b9b/tenor.gif)

If you're not, no worries! You're welcome here!

### Prerequisites

To use this project, you'll need Python (Version 3.8) and Pytest for Unit Tests:

* [Python Installation](https://www.python.org/downloads/)
* [Pytest Installation](https://docs.pytest.org/en/6.2.x/getting-started.html#install-pytest)

### Building program

309pollution is a B-MAT-500 EPITECH module project.

309pollution is about monitoring ambient air quality.

You can use this program as it follows:

```textmate
$> ./309pollution -h
USAGE
        ./309pollution n file x y                                          
DESCRIPTION                                                                
        n       number of points on the grid axis                          
        file    csv file containing the data points x;y;p                  
        x       abscissa of the point whose pollution level we want to know
        y       ordinate of the point whose pollution level we want to know
```

You can also launch unit tests by using the command below at root of the repository:

```textmate
$> coverage run --rcfile=.coveragerc -m --source=sources/ pytest --capture=sys -rA tests/
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/nom4d/EPITECH/309pollution
collected ... items

...

==================================== PASSES ====================================
_____________________                  ...                ______________________
----------------------------- Captured stdout call -----------------------------
...
=========================== short test summary info ============================
...
============================== ... passed in ...s ===============================
$> coverage report -m
// In order to show coverage report
```

### Coding Style

309pollution is developed with Python. EPITECH doesn't impose any Coding Style to this but I tried to be as cleaner as possible.

## Authors

* **Arthur Adam** - [0Nom4D](https://github.com/0Nom4D)

This README file has been created with mdCreator. [Please check the project by clicking this link.](https://github.com/0Nom4D/mdCreator/)
