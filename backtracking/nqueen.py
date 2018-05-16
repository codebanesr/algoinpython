print("Enter the number of queens")
N = int(input())


board = [[0]*N for _ in range(N)]

def is_attacked(i, j):
    for k in range(0, N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    for k in range(0, N):
        for l in range(0, N):
            if ((k+l==i+j) or (k-l==i-j)) and board[k][l]==1:   #if index of some box matches this one such that it has a queen
                return True                                     #it means it is being attaced
    return False


def nqueen(n):
    if n==0:
        return True
    for i in range(N):                      #The board remains the same size that is N only the number of queens "n decreases"              
        for j in range(N):                  #same here
            if board[i][j]!=1 and not(is_attacked(i, j)):
                board[i][j]=1
                if nqueen(n-1)==True:
                    return True
                board[i][j] = 0

    return False


nqueen(N)
for i in board:
    print(i)