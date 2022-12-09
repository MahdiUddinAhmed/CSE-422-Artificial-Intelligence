import math
import random
alpha = -999999999
beta = 9999999


def alpha_beta_prune(list1,Max,a,b):
    A = Alpha(list1,a,b)
    return A

def Alpha(list1,a,b):
    A = len(list1)/2
    Alpha1 = []
    Alpha2 = []
    i = 0

    if A>1:
        while i<A:
            a1 = max(list1[i],a)
            a2 = max(list1[i+1],a)
            Alpha1.append(max(a1,a2))
            i = i+2
        j = int(A)
        while j>=A and j<len(list1):
            a1 = max(list1[j], a)
            a2 = max(list1[j + 1], a)
            Alpha2.append(max(a1, a2))
            j = j+2
    else:
        return max(list1)


    if len(Alpha1+Alpha2)==1:
        return Alpha1+Alpha2
    else:
        return Beta(Alpha1+Alpha2,b)
def Beta(list1,b):
    B = len(list1)/2
    beta1 = []
    beta2 = []
    i = 0

    while i<B:
        a1 = min(list1[i],b)
        a2 = min(list1[i+1],b)
        beta1.append(min(a1,a2))
        i = i+2
    j = int(B)
    while j>=B and j<len(list1):
        a1 = min(list1[j], b)
        a2 = min(list1[j + 1], b)
        beta2.append(min(a1, a2))
        j = j+2


    if len(beta1+beta2)==1:
        return beta1+beta2
    else:
        return Alpha(beta1+beta2,max(beta1+beta2),min(beta1+beta2))




ID =  str(input("Enter Your ID: "))
ID = ID.replace('0','8')
L = len(ID)
Trial = int(ID[3])
if Trial == 0:
    Trial = 8
Max = ID[-2:]
Min = int(ID[4])
HighScore = int(Max[::-1])
Max = math.ceil(int(Max[::-1])*1.5)
T1 = []
j = 0
T2 = []
i = 0

while i<L:
    T1.append(random.randint(Min, Max))
    i = i+1
count1 = int(len(T1))
Depth = 0
while count1!=1:
    Depth = Depth+1
    count1 =count1/2
AB1 = alpha_beta_prune(T1,Max,alpha,beta)
print("Task1")
print("Generated 8 random points between the minimum and maximum point limits: ",T1)
if AB1>HighScore:
    print('The Winner is Optimus Prime')
else:
    print("The Winner is Megatron")


#Task2---------------------------------------------------------------------------
Count2 = 0
while j<Trial:
    random.shuffle(T1)
    AB2 = alpha_beta_prune(T1,Max,alpha,beta)
    if AB2>HighScore:
        Count2 +=1
    T2 = T2 + [AB2]
    j = j+1
print("Task2")
print("List of all points values from each shuffles: ",T2)
AB3 = alpha_beta_prune(T2,Max,alpha,beta)
print("The maximum value of all shuffles: ", AB3)
print(AB3)
print("Won ",Count2, " Times out of 8 time")
