# Empty List to hold the 2D Array
List1 = []
# Reading the I/O file
with open('input.txt', 'r') as f:
    # line by line Iteration
    for line in f:
        a = line.split()  # converting every line to a list
        List1.append(a)  # adding the lists to another list
f.close()

# Empty List to hold the 2D Array
List2 = []
# Reading the I/O file
with open('input1.2.txt', 'r') as f:
    # line by line Iteration
    for line in f:
        a = line.split()  # converting every line to a list
        List2.append(a)  # adding the lists to another list
f.close()

# Output check
'''
for i in List1:
    print(i)
'''


# Main function to check max affected
def affected(matrix):
    """
    a = matrix
    return a
    """
    # adjacent cell co ordinates
    xi = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    yi = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    r = len(matrix)  # row size
    c = len(matrix[0])  # column size

    def Navigate(i, j, matrix, count):

        # check if not Y
        if matrix[i][j] != 'Y':
            return count

        # if Y, mark visited
        count += 1
        matrix[i][j] = 0
        # recursively check up down left right corner for Y to find the maximum area
        for x, y in zip(xi, yi):
            if 0 <= i + x < r and 0 <= y + j < c:
                count = max(count, Navigate(i + x, y + j, matrix, count))  # recursive call
        return count

    max_cells = 0
    # find max region
    for i in range(r):
        for j in range(c):
            max_cells = max(max_cells, Navigate(i, j, matrix, 0))
    return max_cells


print(affected(List1))
print(affected(List2))
