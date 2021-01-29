# Third party modules
from tabulate import tabulate
import pandas


def print_state(generation, generation_idx, fitness):
    '''
    Function print_state.
    Print all data of the generation state.
    '''
    print('Generation {} >> Fitness: {}'.format(generation_idx, fitness))
    print(tabulate(pandas.DataFrame(generation,
                                    ['Person 1', 'Person 2', 'Person 3'],
                                    ['Fill', 'Medium', 'Empty']),
                   headers=['Fill', 'Medium', 'Empty'],
                   tablefmt='orgtbl'), end='\n\n')
