import json
import random


def get_flow_matrix(filename, number_of_machines):
    data = json.load(open(filename))

    flow_matrix = [[0 for _ in range(number_of_machines)] for _ in range(number_of_machines)]
    for d in data:
        flow_matrix[d['source']][d['dest']] = d['amount']

    return flow_matrix


def get_cost_matrix(filename, number_of_machines):
    data = json.load(open(filename))

    cost_matrix = [[0 for _ in range(number_of_machines)] for _ in range(number_of_machines)]
    for d in data:
        cost_matrix[d['source']][d['dest']] = d['amount']

    return cost_matrix

def get_random_coordinates(width, length, number_of_machines):
    coordinates = []
    for m in range(number_of_machines):
        while True:
            new_coordinates = random.randrange(0, width), random.randrange(0, length)
            if new_coordinates not in coordinates:
                coordinates.append(new_coordinates)
                break

    return coordinates
def calculate_fitness(width, length, )