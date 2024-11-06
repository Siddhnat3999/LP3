def issafe(board,row,col):                              #1
    for i in range(row):
        if board[i]==col or abs(board[i]-col)==abs(i-row):  #difference in their rows is equal to the difference in their columns for diagonal
            return False
    return True


def solve(board,row):                                   #2 base case-> loop->issafe->
    if row==8:
        print_board(board)
        return
    
    for i in range(8):
        if(issafe(board,row,i)):
            board[row]=i
            solve(board,row+1)
            board[row]=-1

def print_board(board):                                 #3
    for i in range(8):
        row=['*']*8
        row[board[i]]='Q'
        print(' '.join(row))        #' '.join(row) converts the row list into a single string with each element separated by a space
    print()

board=[-1]*8                                            
board[0]=0
solve(board,1) #caliing func from row one bcs already 1 queen is placed
# O(N!),O(N)