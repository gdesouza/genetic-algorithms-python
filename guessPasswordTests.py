#!/usr/bin/python3
import datetime
import genetic
import unittest
import random

class GuessPasswordTests(unittest.TestCase):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."

    def test_onemax(self):
        target = "1"* 100
        self.geneSet = "01"
        self.guess_password(target)

    def randomTest(self):
        length = 150
        target = ''.join(random.choice(self.geneSet) for _ in range (length))
        self.guess_password(target)

    # def test_For_I_am_fearfully_and_wonderfully_made(self):
    #     target = "For I am fearfully and wonderfully made."
    #     self.guess_password(target)

    # def test_Hello_World(self):
    #     target = "Hello World!"
    #     self.guess_password(target)

    # def test_benchmark(self):
    #     genetic.Benchmark.run(self.randomTest)

    def guess_password(self, target):
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(candidate):
            display(candidate, startTime)

        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneSet, fnDisplay)

        self.assertEqual(''.join(best.Genes), target)

def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t{}\t{}".format(
        ''.join(candidate.Genes), 
        candidate.Fitness, timeDiff))

if __name__ == '__main__':
    unittest.main()