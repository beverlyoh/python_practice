## TASK 1

# given a 5x5 grid, add the last column and row, then flip the card at the
# coordinate specified by the user

five_by_five_grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','X','X'],
    ['X','0','0','X','X'],
]

# # first step is to add colum 6 and row 6
# grid should look like this
# six_by_six_grid = [           
#     ['X','0','X','X','X','0'],
#     ['X','X','0','0','0','0'],
#     ['X','0','X','0','X','X'],
#     ['0','X','X','X','X','0'],
#     ['X','0','0','X','X','X'],
#     ['0','0','X','X','0','0'],
# ]

# output the grid to the user & add col 6
rowX = [0] * 6 
colX = [0] * 6
print('Choose a card to flip in this 5 x 5 grid')
for index, list in enumerate(five_by_five_grid):
    print(list) # output grid to user
    
    rowX[index] = list.count('X')
    if rowX[index] % 2 == 0:
        list.append('0')
    else:
        list.append('X')

    for index, item in enumerate(list):
        if item == 'X':
            colX[index] += 1
        else:
            colX[index] +=0    

# add row 6 & output the new grid
five_by_five_grid.append([]) 
for index, num in enumerate(colX):
    if num % 2 == 0:
        five_by_five_grid[5].append('0')
    else:
        five_by_five_grid[5].append('X')
    #print(five_by_five_grid[index]) # check 6 x 6 grid

# print(rowX)
# print(colX) # for checking, do not output

# # ask the user for the coordinate of the card to flip
flipCoords = input('Please input the coordinates of the card to flip as x,y: ')
x = int(flipCoords[0])
y = int(flipCoords[2])
if x > 5 or y > 5:
    flipCoords = input('Please input the coordinates as x,y: ')

flippedGrid = five_by_five_grid
if flippedGrid[x][y] == 'X':
    flippedGrid[x][y] = '0'
else:
    flippedGrid[x][y] = 'X'

# output the grid with the flipped card
for row in range(0,5):
    print(flippedGrid[row][:5])
    

## TASK 2
# given a six by six grid, work out what card was flipped
rowX2 = [0] * 6
colX2 = [0] * 6
flippedCoord = []
for index, list in enumerate(flippedGrid):
    print(flippedGrid[index]) # view flipped grid
   
    rowX2[index] = list.count('X')
    if rowX2[index] % 2 != 0:
        flippedCoord.append(index)

    for index, item in enumerate(list):
        if item == 'X':
            colX2[index] += 1
        else:
            colX2[index] +=0    

for index, y in enumerate(colX2):
    if y % 2 != 0:
        flippedCoord.append(index)

# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)
print('(' + str(flippedCoord[0]) + ',' + str(flippedCoord[1]) + ')')