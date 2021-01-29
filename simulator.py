# Local modules
from utils import print_state
# Third party modules
import numpy as np
from itertools import product, combinations


def get_first_generation():
    """
    Function get_first_generation.
    Return a matrix representational of the first generation.
    """
    return np.array([
        [7, 0, 0],
        [0, 7, 0],
        [0, 0, 7]
    ])


def get_personal_fitness(person):
    """
    Function get_personal_fitness.
    Return a matrix representational of the first generation.
    """
    fill, medium, empty = person
    return 1 - (abs(3.5 - fill - (0.5 * medium))/3.5)


def get_generation_fitness(generation):
    """
    Function get_generation_fitness.
    Return a matrix representational of the first generation.
    """
    return sum(map(get_personal_fitness, generation))


def search_best_generation(generations):
    """
    Function search_best_generation.
    Take a list of generations and return the index of generation
    with max fitness and the fitness of this generation.
    """
    idx, fitness = 0, 0
    for i, generation in enumerate(generations):
        aux_fitness = get_generation_fitness(generation)
        if aux_fitness > fitness:
            idx = i
            fitness = aux_fitness
    return idx, fitness


def get_next_generation(generation):
    """
    Function get_next_generation.
    Take a generation and return the next one, genering all posibilities
    and selecting the best option.
    """
    posibilities = []

    for option in combinations((0, 1, 2), 2):
        person_a, person_b = generation[option[0]], generation[option[1]]

        for change_a, change_b in product([0, 1, 2], [0, 1, 2]):
            if person_a[change_a] > 0 and person_b[change_b] > 0:
                new_person_a, new_person_b = person_a, person_b
                new_person_a[change_a] -= 1
                new_person_a[change_b] += 1
                new_person_b[change_b] -= 1
                new_person_b[change_a] += 1
                new_generation = generation.copy()
                new_generation[option[0]] = new_person_a
                new_generation[option[1]] = new_person_b
                posibilities.append(new_generation)

    idx, fitness = search_best_generation(posibilities)

    return posibilities[idx], fitness


def simulate():
    """
    Function simulate.
    Run all simulation, show all steps and return the solution.
    """
    generation_counter = 0
    generation = get_first_generation()
    fitness = 0
    print_state(generation, 0, get_generation_fitness(generation))

    while fitness != 3:
        generation, fitness = get_next_generation(generation)
        generation_counter += 1
        print_state(generation, generation_counter, fitness)

    return generation
