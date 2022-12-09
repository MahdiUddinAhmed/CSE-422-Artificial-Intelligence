import random

def GA(list1,Range):
    C = -1
    A = 0
    D = mutation(list1,Range)
    B = D[2]
    count = 0
    if B!= 0:
        while B!=0 and count<=10000:
            count = count +1
            C = mutation(list1,Range)
            B=C[2]

        if C[2]==0:
            return C
        else:
            return -1

def fitness(list1,target):
    S = 0
    for i in list1:
        S = S+i
    B = abs((target-S)/target)
    return B


def mutation(list1,Range):
    Child = crossover(list1)
    sample = []
    a = len(list1)-1
    for i in range(0,a):
        if Child[i] ==1:
            sample.append(list1[i])

    Z = fitness(sample, int(Range))
    return Child,sample,Z

def crossover(List1):
    half = len(List1)//2
    X = []
    Y = []
    for i in range(0,len(List1)):
        X.append(random.randint(0, 1))
        Y.append(random.randint(0, 1))


    X = X[half:]
    Y = Y[:half]
    XY = X + Y
    return(XY)

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
    A = GA(Genes,Part1[0][1])
    print(A)
    Names = []
    Score = 0

    for i in Part2:
        Names.append(i[0])
    if A!= -1:
        Score = A[0]

    print(Names, Score)

with open('Output2.txt','w') as w:

    w.write(str(Names))
    w.write('\n')
    if A!= -1:
        for i in Score:
            w.write(str(i))
            w.write(' ')
    else:
        w.write(str(A))