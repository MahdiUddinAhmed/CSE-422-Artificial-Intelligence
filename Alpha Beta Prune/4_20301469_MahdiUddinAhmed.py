import math
import random
'''
lst1 = [66, 74, 14, 73, 19, 26, 32, 40]
A = int(len(lst1))
#print(A)
Z = math.log2(A).is_integer()
D = math.log2(A)%2
#print(D)
if Z == False:
    while Z == False:
        lst1.append(0)
        A = int(len(lst1))
        Z = math.log2(A).is_integer()

#print(lst1)

#print(Depth)
'''

def alpha_beta(lst,depth):
    A = int(len(lst))
    M = A//2

    if A==1:
        return 'invalid'
    if A == 2:
        return max(lst)
    Ch1 = Beta(lst[:M],depth-1,0)
    Ch2 = Beta(lst[M:],depth-1,0)
    return max(Ch1,Ch2)
def Beta(lst,depth,pos):
    A = int(len(lst))
    M = A//2
    #print(lst)
    #print('Beta')
    if depth ==1:
        return min(lst[pos],lst[pos+1])
    else:
        B1 = Alpha(lst[:M],depth-1,pos)
        B2 = Alpha(lst[M:], depth-1,pos)
        return min(B1,B2)

def Alpha(lst,depth,pos):
    A = int(len(lst))
    M = A // 2
    #print(lst)
    #print('ALpha')
    if depth == 1:
        return max(lst[pos],lst[pos+1])
    else:
        A1 = Beta(lst[:M], depth - 1, pos)
        A2 = Beta(lst[M:], depth - 1, pos)
        return max(A1, A2)

ID =  str(input("Enter Your ID: "))

ID = ID.replace('0','8')

L = len(ID)
R = int(ID[3])
if R == 0:
    R = 8
Max = ID[-2:]
High = int(Max[::-1])
Max = math.ceil(int(Max[::-1])*1.5)
Min = int(ID[4])


M = []
j = 0

X = []
i = 0
while i<L:
    X.append(random.randint(Min, Max))
    i = i+1

count = int(len(X))
Depth = 0

while count!=1:
    Depth = Depth+1
    count =count/2
A1 =alpha_beta(X,Depth)
print("Task1")
print("Generated 8 random points between the minimum and maximum point limits: ",X)
if A1>High:
    print('The Winner is Optimus Prime')
else:
    print("The Winner is Megatron")
C = 0
while j<R:
    random.shuffle(X)
    A = alpha_beta(X,Depth)
    if A>High:
        C +=1
    M = M + [A]
    j = j+1
print("Task2")
print("List of all points values from each shuffles: ",M)
A2 = alpha_beta(M,Depth)
print("The maximum value of all shuffles: ", A2)
print(A2)
print("Won ",C, " Times out of 8 time")