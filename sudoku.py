board = [
    [ 0 , 0 , 0 , 7 , 0 , 0 , 4 , 0 , 6 ],
    [ 0 , 0 , 9 , 0 , 0 , 0 , 0 , 0 , 0 ],
    [ 6 , 0 , 8 , 0 , 4 , 0 , 0 , 0 , 1 ],
    [ 3 , 0 , 6 , 2 , 0 , 0 , 0 , 8 , 0 ],
    [ 0 , 9 , 0 , 0 , 6 , 0 , 0 , 0 , 0 ],
    [ 0 , 7 , 0 , 0 , 0 , 0 , 0 , 0 , 3 ],
    [ 0 , 0 , 0 , 0 , 0 , 5 , 0 , 2 , 0 ],
    [ 0 , 3 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
    [ 1 , 0 , 4 , 0 , 7 , 0 , 0 , 0 , 8 ]
]

def solve(boa):
    find = find_empty(boa)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):   #cycle through values 1 - 9
        if valid(boa, i, (row, col)):   #if valid plug in num
            boa[row][col] = i

            if solve(boa):  #recursively keep calling solve untill all boxes are filled
                return True
            
            boa[row][col] = 0   #else keep box empty
            
    return False

def valid(boa, num, pos):
    #Check row
    for i in range(len(boa[0])):    #length of column
        if boa[pos[0]][i] == num and pos[1] != 1:#check through each row
            return False    #for a num that matches the one inputted

    #Check coloumn
    for i in range(len(boa)):  #length of row
       if boa[i][pos[1]] == num and pos[0] != 1:
            return False    #checks all columns for equal numbers
    #Check box
    box_x = pos[1] // 3  #gives values 0,1,2
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):#row 1,2,3 of each box
        for j in range(box_x*3, box_x*3 + 3):#col 1,2,3 of each box
            if boa[i][j] == num and (i,j) != pos:
                return False    #if num match return false

    return True
                    

def print_board(boa):
    
    for i in range(len(boa)):   #every third row followed by a line
        if i % 3 == 0 and i != 0:   #seperate baord into boxes
            print("- - - - - - - - - - - - - ")

        for j in range(len(boa[0])):    #every third column add a line
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(boa[i][j])
            else:
                print(str(boa[i][j]) + " ", end="")

def find_empty(boa):
    for i in range(len(boa)):
        for j in range(len(boa[0])):
            if boa[i][j] == 0:  #empty box represented as 0
                return (i, j)   #return position of empty box
    return None #if no squares are empty

print_board(board)
print("\n")
print("Solving ...")
print("\n")
solve(board)
print_board(board)
