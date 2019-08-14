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
# six_by_six_grid = [
#     ['X','0','X','X','X','0'],
#     ['X','X','0','0','0','0'],
#     ['X','0','X','0','X','X'],
#     ['0','X','X','X','X','0'],
#     ['X','0','0','X','X','X'],
#     ['0','0','X','X','0','0'],
# ]

# output the grid to the user
# for index, num in enumerate(five_by_five_grid):
#     print(index, num)

# # ask the user for the coordinate of the card to flip
# # e.g. input could be: (0,2)
# print(five_by_five_grid[0][2])


# def flipGrid(x,y):
counter = 0 
while counter < len(five_by_five_grid):
    myCount = five_by_five_grid[counter].count('X')
    
    if myCount % 2 == 0: # if even
        five_by_five_grid[counter].append('0') # add an 'X' if odd
    else:      
        five_by_five_grid[counter].append('X') # add an 'X' if odd
    
    counter = counter + 1
    print(five_by_five_grid[counter])

#     #coord = input('Please input coordinate from 1 to 5 as (x,y)')
    
#     # flip the coordinate specified
#     if five_by_five_grid[x][y] == '0':
#         six_by_six_grid[x][y] = 'X'
#     else:
#         six_by_six_grid[x][y] == '0'
    
#     # lets see where is is flipped
# numberOfOdds = [] # define empty list
# for num in range(1,6):
#             countX = six_by_six_grid[num].count('X')
#             numberOfOdds += countX

    #  five_by_five_grid[][]

#print(flipGrid(2,3))
# output the grid with the flipped card

## TASK 2

# given a six by six grid, work out what card was flipped

# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)