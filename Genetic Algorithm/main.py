
import numpy as np
import random

def GA(list1,solutionR,generation):

    def fitness(list,solutionR):
        s = 0
        c = 0
        for i in list:
            a = sum(i)
            if a == solutionR:
                s = solutionR
                c =+ 1
                return s,i
        if c==0:
            return -1,i


    def crossover(list1,solutionR,generation):
        ChromosomeSample = []
        for i in range(0, generation):
            population = random.randint(0, len(list1))
            parents = random.sample(list1, population)
            ChromosomeSample.append(parents)
            Solution = fitness(ChromosomeSample, solutionR)
        return Solution

    return crossover(list1,solutionR,generation)


with open('input1.txt', 'r') as f:
    Input = []
    for lines in f:
        Input.append(lines.strip().split())

    Part1 = Input[:1]


    for i in Input:
        if i == []:
            Input.remove(i)

    Part2 = Input[1:]

    for i in Part1:
        i[0] = int(i[0])
        i[1] = int(i[1])

    Genes = []
    for i in Part2:
        Genes.append(int(i[1]))
    print(Genes)
    A = GA(Genes,Part1[0][1], 10000)
    Zero = []
    Solve = ''
    for i in range(len(Genes)):
        Zero.append(0)
    Names = []
    if A[0] == -1:
        print(-1)
    else:
        for i in Genes:
            for j in Part2:
                if str(i) == j[1]:
                    Names.append(j[0])

        for i in A[1]:
            for j in Part2:
                if str(i) == j[1]:
                    Idx = Genes.index(i)
                    Zero[Idx] = 1
        print(A[1])
        print(Names)
        print(Zero)

f.close()
