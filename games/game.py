class Move:
    def __init__(self,x,y):
        self.x=x
        self.y=y



class Game(object):
    def __init__(self,size,con_size,depth):
        self.board=[]
        for i in range(size):
            self.board.append(['_']*size)
        self.size=size
        self.con_size=con_size
        self.player='x'
        self.computer='o'
        self.depthcutoff=depth

    def cutoff(self,depth):
        if depth>=self.depthcutoff:
            return True
        else:
            return False


    def utility(self):
        pass

    def heuristic_evaluation_function(self):
        pass

    def movesLeft(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j]=='_':
                    return True
        return False

    def minimax(self,depth,isMax,alpha,beta):
        score=self.utility()
        if score==1 or score==-1:
            return score
    #     if cutoff(self.board,depth):
    #         temp=heuristic_evaluation_function(self.board)
    # #         print(self.board,temp)
    #         return temp
        else:
            if self.movesLeft()==False:
                return 0
            else:
                if isMax:
                    best=-1000
                    for i in range(self.size):
                        for j in range(self.size):
                            if self.board[i][j]=='_':
                                self.board[i][j]=self.computer
    #                             print(i,j)
    #                             print(best)
                                temp=self.minimax(depth+1,~isMax,alpha,beta)
    #                             print(best,i,j,temp)
                                best=max(best,temp)
                                alpha=max(alpha,best)
    #                             print(best)
                                self.board[i][j]='_'
                                if beta<=alpha:
                                    break
                                
                else:
                    best=1000
                    for i in range(self.size):
                        for j in range(self.size):
                            if self.board[i][j]=='_':
                                self.board[i][j]=self.player
    #                             print(i,j)
    #                             print(best)
                                temp=self.minimax(depth+1,~isMax,alpha,beta)
    #                             print(best,i,j,temp)
                                best=min(best,temp)
                                beta=min(beta,best)
                                self.board[i][j]='_'
                                if beta<=alpha:
                                    break
                                
                return best

    def FindBestMove(self):
        best_move_val=-1000
        best_move=Move(-1,-1)
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j]=='_':
                    self.board[i][j]=self.computer
                    move_val=self.minimax(0,False,-1000,1000)
                    print(self.board,move_val)
                    self.board[i][j]='_'
                    if move_val>best_move_val:
                        best_move_val=move_val
                        best_move.x=i
                        best_move.y=j
        return best_move

    def game_move(self,pos):
        print("================================================================")
        self.print_board()
        print("================================================================")
        self.player='x'
        self.computer='o'
        x,y=pos[0],pos[1]
        self.board[x][y]=self.player
        self.print_board()
        output=0
        print("================================================================")
        move_computer=self.FindBestMove()
        self.board[move_computer.x][move_computer.y]=self.computer
        self.print_board()
        print("================================================================")

        return move_computer

    def clear_board(self):
        for i in range(self.size):
            self.board=[]
            self.board.append(['_']*self.size)

    def print_board(self):
        for i in range(self.size):
            print(self.board[i])


class TicTacToe(Game):

    def __init__(self):
        super(TicTacToe,self).__init__(3,3,3)

    def heuristic_evaluation_function(self):
        self.player='x'
        self.computer='o'
        heuristic=0
        for i in range(self.size):
            if self.board[i][0]==self.board[i][1] and self.board[i][1]==self.board[i][2]:
                if self.board[i][0]==self.player:
                    heuristic-=1000
                elif self.board[i][0]==self.computer:
                    heuristic+=1000
    #     print(heuristic)
        for j in range(self.size):
            if self.board[0][j]==self.board[1][j] and self.board[1][j]==self.board[2][j]:
                if self.board[0][j]==self.player:
                    heuristic-=1000
                elif self.board[0][j]==self.computer:
                    heuristic+=1000
    #     print(heuristic)
        if self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2]:
            if self.board[0][0]==self.player:
                heuristic-=1000
            elif self.board[0][0]==self.computer:
                heuristic+=1000
    #     print(heuristic)
        if self.board[0][2]==self.board[1][1] and self.board[1][1]==self.board[2][0]:
            if self.board[0][2]==self.player:
                heuristic-=1000
            elif self.board[0][2]==self.computer:
                heuristic+=1000
    #     print(heuristic)
        for k in range(self.size):
            if self.board[k][0]==self.board[k][1] and self.board[k][2]=='_':
                if self.board[k][0]==self.player:
                    heuristic-=10
                elif self.board[k][0]==self.computer:
                    heuristic+=10
            elif self.board[k][1]==self.board[k][2] and self.board[k][0]=='_':
                if self.board[k][1]==self.player:
                    heuristic-=10
                elif self.board[k][1]==self.computer:
                    heuristic+=10
            if self.board[k][0]==self.board[k][1] and self.board[k][2]=='o' and self.board[k][0]=='x':
                heuristic+=100
            elif self.board[k][1]==self.board[k][2] and self.board[k][0]=='o' and self.board[k][1]=='x':
                heuristic+=100
            elif self.board[k][0]==self.board[k][2] and self.board[k][0]=='x' and self.board[k][1]=='x':
                heuristic+=100
    #     print(heuristic)
        for l in range(self.size):
            if self.board[0][l]==self.board[1][l] and self.board[2][l]=='_':
                if self.board[0][l]==self.player:
                    heuristic-=10
                elif self.board[0][l]==self.computer:
                    heuristic+=10
            elif self.board[1][l]==self.board[2][l] and self.board[0][l]=='_':
                if self.board[1][l]==self.player:
                    heuristic-=10
                elif self.board[1][l]==self.computer:
                    heuristic+=10
            if self.board[0][l]==self.board[1][l] and self.board[2][l]=='o' and self.board[0][l]=='x':
                heuristic+=100
            elif self.board[1][l]==self.board[2][l] and self.board[1][l]=='x' and self.board[0][l]=='o':
                heuristic+=100
            elif self.board[0][l]==self.board[2][l] and self.board[0][l]=='x' and self.board[1][l]=='o':
                heuristic+=100
    #     print(heuristic)
        if self.board[0][0]==self.board[1][1] and self.board[0][0]=='x' and self.board[1][1]=='o':
            heuristic+=100
        elif self.board[0][0]==self.board[2][2] and self.board[0][0]=='x' and self.board[1][1]=='o':
            heuristic+=100
        elif self.board[1][1]==self.board[2][2] and self.board[1][1]=='x' and self.board[0][0]=='o':
            heuristic+=100
        if self.board[0][2]==self.board[1][1] and self.board[0][2]=='x' and self.board[2][0]=='o':
            heuristic+=100
        elif self.board[2][0]==self.board[1][1] and self.board[2][0]=='x' and self.board[0][2]=='o':
            heuristic+=100
        elif self.board[0][2]==self.board[2][0] and self.board[0][2]=='x' and self.board[1][1]=='o':
            heuristic+=100
        if (self.board[0][0]==self.board[1][1] and self.board[2][2]=='_') or (self.board[1][1]==self.board[2][2] and self.board[0][0]=='_'):
            if self.board[1][1]==self.player:
                heuristic-=10
            elif self.board[1][1]==self.computer:
                heuristic+=10
    #     print(heuristic)
        if (self.board[0][2]==self.board[1][1] and self.board[2][0]=='_') or (self.board[1][1]==self.board[2][0] and self.board[0][2]=='_'):
            if self.board[1][1]==self.player:
                heuristic-=10
            elif self.board[1][1]==self.computer:
                heuristic+=10
    #     print(heuristic)
        if (self.board[0][0]==self.board[1][1] and self.board[0][0]=='_'):
            if self.board[2][2]==self.player:
                heuristic-=1
            elif self.board[2][2]==self.computer:
                heuristic+=1
        elif (self.board[1][1]==self.board[2][2] and self.board[1][1]=='_'):
            if self.board[0][0]==self.player:
                heuristic-=1
            elif self.board[0][0]==self.computer:
                heuristic+=1
    #     print(heuristic)
        if self.board[0][2]==self.board[1][1] and self.board[1][1]=='_':
            if self.board[2][0]==self.player:
                heuristic-=1
            elif self.board[2][0]==self.computer:
                heuristic+=1
        elif self.board[1][1]==self.board[2][0] and self.board[1][1]=='_':
            if self.board[0][0]==self.player:
                heuristic-=1
            elif self.board[0][0]==self.computer:
                heuristic+=1
            
    #     print(heuristic)
        for r in range(self.size):
            count=0
            for c in range(self.size):
                if self.board[r][c]=='_':
                    count+=1
                else:
                    key=self.board[r][c]
            if count==2:
                if key==self.player:
                    heuristic-=1
                elif key==self.computer:
                    heuristic+=1
    #     print(heuristic)
        for g in range(self.size):
            count=0
            for h in range(self.size):
                if self.board[h][g]=='_':
                    count+=1
                else:
                    key=self.board[h][g]
            if count==2:
                if key==self.player:
                    heuristic-=1
                elif key==self.computer:
                    heuristic+=1
        
    #     print(heuristic)
        return heuristic
        
    def utility(self):
        for i in range(self.size):
            if self.board[i][0]==self.board[i][1] and self.board[i][1]==self.board[i][2]:
                if self.board[i][0]==self.player:
                    return  -1
                elif self.board[i][0]==self.computer:
                    return 1
        for j in range(self.size):
            if self.board[0][j]==self.board[1][j] and self.board[1][j]==self.board[2][j]:
                if self.board[0][j]==self.player:
                    return -1
                elif self.board[0][j]==self.computer:
                    return 1
        if self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2]:
            if self.board[0][0]==self.player:
                return -1
            elif self.board[0][0]==self.computer:
                return 1
        if self.board[0][2]==self.board[1][1] and self.board[1][1]==self.board[2][0]:
            if self.board[0][2]==self.player:
                return -1
            elif self.board[0][2]==self.computer:
                return 1
        return 0

    
        
    
    

    


        
    
        

    
            
