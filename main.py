# Local modules
from simulator import simulate
# Third party modules
from tabulate import tabulate
import pandas


def main():
    """
    Function main.
    Call to function simulate and present the result.
    """
    print('Solving...')
    simulate()
    print('Problem solved!', end='\n\n')


if __name__ == '__main__':
    main()
