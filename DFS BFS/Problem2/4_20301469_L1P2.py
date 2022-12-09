List1 = []
# Reading the I/O file
with open('Question2input1.txt', 'r') as f:
    # line by line Iteration
    List2 = []
    for line in f:
        b = line.strip()
        List2.append(b)
        a = line.split()  # converting every line to a list
        List1.append(a)  # adding the lists to another list

f.close()
List3 = []
# Reading the I/O file
with open('Question2input2.txt', 'r') as f:
    # line by line Iteration
    List4 = []
    for line in f:
        b = line.strip()
        List4.append(b)
        a = line.split()  # converting every line to a list
        List3.append(a)  # adding the lists to another list

f.close()
List1 = List1[2:]
'''
for i in List1:
    print(i)
'''
List2 = List2[0:2]
#print(List2)
count = 0

List3 = List3[2:]
'''
for i in List1:
    print(i)
'''
List4 = List4[0:2]
#print(List2)


def attack(Range, matrix):
    # up down left right co ordinates
    global A, Cc
    xi = [0, 1, 0, 0, -1]
    yi = [1, 0, 0, -1, 0]
    r = int(Range[0])  # row size
    c = int(Range[1])  # column size

    # Navigation
    def dead(i, j, matrix, r, c, count):
        Cc = 0
        # If alien found
        if matrix[i][j] == 'A':

            # check all children of the node
            for x, y in zip(xi, yi):
                if 0 <= i + x < r and 0 <= y + j < c and matrix[i + x][j + y] == 'H':
                    # explore the children
                    matrix, Cc = dead(i + x, j + y, matrix, r, c, count)
                    matrix[i + x][j + y] = 'A'
                # else finish the attack, go back to parent, explore another child and update the counter
                count += 1

            '''
            if i<=r-1 and j+1<=c-1 and matrix[i][j+1]=='H':
                matrix[i][j+1] = 'A'
            if i+1<=r-1 and j<=c-1 and matrix [i+1][j]=='H':
                matrix[i+1][j]='A'
            if i-1>=0 and matrix[i-1][j]=='H':
                matrix[i-1][j]='A'
            if j-1>=0 and matrix[i][j-1]=='H':
                matrix[i][j-1]='A'
        '''

        return matrix, count

    # Start BFS
    for i in range(r):
        for j in range(c):
            A, Cc = dead(i, j, matrix, r, c, count)
    return A, Cc


H = 0
# BFS call
B, Cc = attack(List2, List1)
for i in B:
    for j in i:
        if j == 'H':
            H += 1
if H==0:
    print('No one  Survived')
else:
    print(H, 'Survived')
print('Time:',Cc,'minutes')

H = 0
# BFS call
B, Cc = attack(List4, List3)
for i in B:
    for j in i:
        if j == 'H':
            H += 1
if H==0:
    print('No one  Survived')
else:
    print(H, 'Survived')
print('Time:',Cc,'minutes')