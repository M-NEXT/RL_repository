#!/usr/bin/env python
# coding: utf-8

# In[1]:


game = []
for i in range(3):
    game = game + [[0,0,0]]

points = {'Human' : -1 , 'AI' : 1 , 'Tie' : 0}


# In[2]:


def winner(game):
    #HORIZONTAL WIN
    for row in game:
        if row.count(row[0]) == len(row) and row[0] == 1:
            return 'Human'
        elif row.count(row[0]) == len(row) and row[0] == 2:
            return 'AI'
    
    
    #VERTICAL WIN
    for column in range(len(game)):
        col = []
        for row in game:
            col = col + [row[column]]
        if col.count(col[0]) == len(col) and col[0] == 1:
            return 'Human'
        elif col.count(col[0]) == len(col) and col[0] == 2:
            return 'AI'
    
    
    #DIAGONAL WINS    
    diag_1 = []
    diag_2 = []
    for index in range(len(game)):
        diag_1 = diag_1 + [game[index][index]]
        diag_2 = diag_2 + [game[index][len(game) - index - 1]]

    if diag_1.count(diag_1[0]) == len(diag_1) and diag_1[0] == 1:
        return 'Human'
    elif diag_1.count(diag_1[0]) == len(diag_1) and diag_1[0] == 2:
        return 'AI'
    if diag_2.count(diag_2[0]) == len(diag_2) and diag_2[0] == 1:
        return 'Human'
    elif diag_2.count(diag_2[0]) == len(diag_2) and diag_2[0] == 2:
        return 'AI'
    
    
    #TIE GAME
    tie = []
    for rows in game:
        tie = tie + rows
    if tie.count(0) == 0:
        return 'Tie'


# In[3]:


def minimax(game, player):
    result = winner(game)
    if result != None:
        score = points[result]
        return score
    
    if(player == 'AI'):
        BestScore = -10
        for rnum, rows in enumerate(game):
            for cnum, cols in enumerate(rows):
                if game[rnum][cnum] == 0:
                    game[rnum][cnum] = 2
                    score = minimax(game, 'Human')
                    game[rnum][cnum] = 0
                    
                    BestScore = max(score,BestScore)
        return BestScore
    
    else:
        BestScore = 10
        for rnum, rows in enumerate(game):
            for cnum, cols in enumerate(rows):
                if game[rnum][cnum] == 0:
                    game[rnum][cnum] = 1
                    score = minimax(game, 'AI')
                    game[rnum][cnum] = 0
                    
                    BestScore = min(score,BestScore)
        return BestScore
                    


# In[4]:


def main(game):
    game = []
    for i in range(3):
        game = game + [[0,0,0]]
    print(game[0][0],'|',game[0][1],'|',game[0][2],'       1  2  3')
    print(game[1][0],'|',game[1][1],'|',game[1][2],' <==>  4  5  6')
    print(game[2][0],'|',game[2][1],'|',game[2][2],'       7  8  9')
    
    points = {'Human' : -1 , 'AI' : 1 , 'Tie' : 0}
    
    
    while True:
        PlayerMove = int(input('Enter your move : '))
        if PlayerMove < 1 or PlayerMove > 9:
            print('Enter a Valid Move')
            continue
        
        PlayerMove = PlayerMove - 1
        row = PlayerMove // 3
        column = (PlayerMove % 3)
        
        if game[row][column] !=0:
            print('Place is occupied, select different move')
            continue
        
        game[row][column] = 1
        
        result = winner(game)
        if result != None:
            if result == 'Tie':
                print('Tie match')
            else:
                print(result, 'won')
            break
            
        BestScore = -10
        BestMove = []
        for rnum, rows in enumerate(game):
            for cnum, cols in enumerate(rows):
                if game[rnum][cnum] == 0:
                    game[rnum][cnum] = 2
                    score = minimax(game, 'Human')
                    game[rnum][cnum] = 0
                    
                    if score > BestScore:
                        BestScore = score
                        BestMove = [rnum, cnum]
                        
        game[BestMove[0]][BestMove[1]] = 2
        
        print(game[0][0],'|',game[0][1],'|',game[0][2],'       1  2  3')
        print(game[1][0],'|',game[1][1],'|',game[1][2],' <==>  4  5  6')
        print(game[2][0],'|',game[2][1],'|',game[2][2],'       7  8  9')
        
        result = winner(game)
        if result != None:
            if result == 'Tie':
                print('Tie match')
            else:
                print(result, 'won')
            break
        


# In[5]:


main(game)


# 
