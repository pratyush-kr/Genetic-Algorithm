import numpy as np
import random as rand

if __name__ == '__main__':
    ch = []
    population = []
    for i in range(50):
        for j in range(5):
            ch += [int(rand.random() * 10)]
        population += [ch]
        ch = []
    print(population)
    sum = 25