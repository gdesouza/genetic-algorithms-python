#!/usr/bin/python3
import unittest
import datetime
import genetic

def get_fitness(genes):
    #return a count the number of 1's in the genes
    return genes.count(1)

def display(candidate, startTime):
    #display the current genes, their fitness, and elapsed time
    timeDiff = datetime.datetime.now() - startTime
    print("{}...{}\t{:3.2f}\t{}".format(
        ''.join(map(str, candidate.Genes[:15])),
        ''.join(map(str, candidate.Genes[-15:])),
        candidate.Fitness,
        timeDiff
    ))

class OneMaxTests(unittest.TestCase):
    def test(self, length=100):
        geneset = [0, 1]
        # Create the helper functions and optimal fitness
        # then call assert that the firness of the result is optimal
        startTime = datetime.datetime.now()

        def fnDisplay(candidate):
            display(candidate, startTime)

        def fnGetFitness(genes):
            return get_fitness(genes)

        optimalFitness = length
        best = genetic.get_best(fnGetFitness, length, optimalFitness, geneset, fnDisplay)
        self.assertEqual(best.Fitness, optimalFitness)

    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.test(4000))

if __name__ == '__main__':
    unittest.main()