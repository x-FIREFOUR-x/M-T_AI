import math
import random


def func1(x):
    return math.cos(x[0]/2) + math.sin(x[0]/4) * math.sin(math.cos(x[0]+1))


def func2(x):
    return x[0] * math.cos(abs(x[1]))


class GeneticAlgo:
    def __init__(self, countGenes, Function, isMaximize):
        self.countPerson = 10
        self.countPopulations = 100
        self.crossChance = 0.99
        self.mutationChance = 0.15

        self.startLine = -4.0
        self.endLine = 1.0

        self.currentPopulation = []

        self.countGenes = countGenes
        self.Function = Function
        self.isMaximize = isMaximize

    def run(self):
        self.getStartPopulation()
        for i in range(self.countPopulations):
            self.print(i)
            self.sortPopulation()
            self.createNewPopulation()

        self.sortPopulation()
        self.print(self.countPopulations)

    def getStartPopulation(self):
        for i in range(self.countPerson):
            newPerson = []
            for j in range(self.countGenes):
                newPerson.append(random.uniform(self.startLine, self.endLine))
            self.currentPopulation.append(newPerson)

    def sortPopulation(self):
        self.currentPopulation.sort(key=lambda person: self.Function(person), reverse=self.isMaximize)

    def createNewPopulation(self):
        newPopulation = []
        for person in self.currentPopulation:
            newPerson = person

                #Cross
            if random.random() < self.crossChance:
                for i in range(self.countGenes):
                    newPerson[i] = (newPerson[i] + self.currentPopulation[0][i]) / 2

                #Mutation
            for i in range(self.countGenes):
                if random.random() < self.mutationChance:
                    newPerson[i] += 0.01

            newPopulation.append(newPerson)

        self.currentPopulation = newPopulation

    def print(self, iteration):
        if( iteration % 5 == 0):
            print("Number Population: ", end="")
            print(iteration, end=": ")
            print(self.currentPopulation[0], end=" = ")
            print(self.Function(self.currentPopulation[0]))



if __name__ == '__main__':
    print("\ny = cos(x/2) + sin(x/4) * sin(cos(x+1))")
    GeneticAlgo(1, func1, False).run()

    print("\nz = x + cos|y|")
    GeneticAlgo(2, func2, True).run()
