# Genetic Algorithm to Solve 8-Queens
Uses a basic genetic algorithm to generate soutions. 

Run with >python3 8-queens.py

There are several command line args, find them with >python3 8-queens.py -h

## Genetic Algorithm Implemlentation Details
The individuals in my GA were represented as an array of integers. Each element in the array was a column and the integers themselves represented the row that the queen was in.

The fitness function was simply how many queen pairs were non-conflicting. A perfect score of 28 represented no conflicts.

Mutation was achieved by picking a random number in an individual and changing it. I chose to allow for a number being randomly changed into itself.

My crossover function was done by taking the two parents and splitting them both at a random point, then creating a child with the two left and right sections of different parents. I did make sure not to split at element 0 or 7, which would create a clone child.

After a generation was checked for any winner individuals, I sorted the population via the fitness function, dropped the bottom half, and then created new individuals by randomly picking two parents to breed until the population was back to full.
