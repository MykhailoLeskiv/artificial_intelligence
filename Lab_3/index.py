from os import system
from tkinter import *

class ChoiceTree():
    def __init__(self):
        self.A = []
        for i in range(3):
            self.A.append([])
            for j in range(3):
                self.A[i].append([])
        self.root = Tk()
        self.root.title('Tic Tac Toe')
        self.root.geometry('400x400')
        self.buttons = []
        for x in range(3):
            self.buttons.append([])
            for y in range(3):
                self.buttons[x].append(Button(self.root, text="", font='arial 48'))
                self.buttons[x][y].place(relx = x/3, rely = y/3, height=400/3, width=400/3)
        self.root.mainloop()
    def ComputersMoveChange(self, x, y):
        self.buttons[x][y]['text'] = 'O'
    def EnemyAttack(self):
        for i, s in enumerate(self.A):
            if s.count('X') == 2 and s.count('O') == 0:
                for j, t in enumerate(s):
                    if t == '-':
                        self.A[i][j] = 'O'
                        self.buttons[i][j]['text'] = 'O'
                        break
                return True
        rut = [self.A[0][0], self.A[1][1], self.A[2][2]]
        if rut.count('X') == 2 and rut.count('O') == 0:
            if self.A[0][0] == '-':
                self.A[0][0] = 'O'
                self.buttons[0][0]['text'] = 'O'
            elif self.A[1][1] == '-':
                self.A[1][1] = 'O'
                self.buttons[1][1]['text'] = 'O'
            else:
                self.A[2][2] = 'O'
                self.buttons[2][2]['text'] = 'O'
            return True
        rut = [self.A[0][2], self.A[1][1], self.A[2][0]]
        if rut.count('X') == 2 and rut.count('O') == 0:
            if self.A[0][2] == '-':
                self.A[0][2] = 'O'
                self.buttons[0][2]['text'] = 'O'
            elif self.A[1][1] == '-':
                self.A[1][1] = 'O'
                self.buttons[1][1]['text'] = 'O'
            else:
                self.A[2][0] = 'O'
                self.buttons[2][0]['text'] = 'O'
            return True
        self.A = [list(i) for i in zip(*self.A)]
        flag = False
        for i, s in enumerate(self.A):
            if s.count('X') == 2 and s.count('O') == 0:
                for j, t in enumerate(s):
                    if t == '-':
                        self.A[i][j] = 'O'
                        self.buttons[j][i]['text'] = 'O'
                        flag = True
                        self.A = [list(i) for i in zip(*self.A)]
                        break
                if flag:
                    return True
        self.A = [list(i) for i in zip(*self.A)]
        return False
    def PlayerError(self):
        for i, s in enumerate(self.A):
            if s.count('O') == 2 and s.count('X') == 0:
                for j, t in enumerate(s):
                    if t == '-':
                        self.A[i][j] = 'O'
                        self.buttons[i][j]['text'] = 'O'
                        break
                return True
        rut = [self.A[0][0], self.A[1][1], self.A[2][2]]
        if rut.count('O') == 2 and rut.count('X') == 0:
            if self.A[0][0] == '-':
                self.A[0][0] = 'O'
                self.buttons[0][0]['text'] = 'O'
            elif self.A[1][1] == '-':
                self.A[1][1] = 'O'
                self.buttons[1][1]['text'] = 'O'
            else:
                self.A[2][2] = 'O'
                self.buttons[2][2]['text'] = 'O'
            return True
        rut = [self.A[0][2], self.A[1][1], self.A[2][0]]
        if rut.count('O') == 2 and rut.count('X') == 0:
            if self.A[0][2] == '-':
                self.A[0][2] = 'O'
                self.buttons[0][2]['text'] = 'O'
            elif self.A[1][1] == '-':
                self.A[1][1] = 'O'
                self.buttons[1][1]['text'] = 'O'
            else:
                self.A[2][0] = 'O'
                self.buttons[2][0]['text'] = 'O'
            return True
        self.A = [list(i) for i in zip(*self.A)]
        flag = False
        for i, s in enumerate(self.A):
            if s.count('O') == 2 and s.count('X') == 0:
                for j, t in enumerate(s):
                    if t == '-':
                        self.A[i][j] = 'O'
                        self.buttons[j][i]['text'] = 'O'
                        flag = True
                        self.A = [list(i) for i in zip(*self.A)]
                        break
                if flag:
                    return True
        self.A = [list(i) for i in zip(*self.A)]
        return False
    def Winning(self):
        for i, s in enumerate(self.A):
            if s.count('O') == 3:
                return True
        rut = [self.A[0][0], self.A[1][1], self.A[2][2]]
        if rut.count('O') == 3:
            return True
        rut = [self.A[0][2], self.A[1][1], self.A[2][0]]
        if rut.count('O') == 3:
            return True
        self.A = [list(i) for i in zip(*self.A)]
        for i, s in enumerate(self.A):
            if s.count('O') == 3:
                self.A = [list(i) for i in zip(*self.A)]
                return True
        self.A = [list(i) for i in zip(*self.A)]
        return False
    def firstMove(self):
        if self.A[0][0] == 'X' or self.A[0][2] == 'X' or self.A[2][0] == 'X' or self.A[2][2] == 'X':
            self.A[1][1] = 'O'
            self.buttons[1][1]['text'] = 'O'
            self.printBoard()
            self.playerMove()
            self.secondMove1()
        elif self.A[1][1] == 'X':
            self.A[0][0] = 'O'
            self.buttons[0][0]['text'] = 'O'
            self.printBoard()
            self.playerMove()
            self.secondMove2()
        elif self.A[0][1] == 'X' or self.A[1][0] == 'X':
            self.A[0][0] = 'O'
            self.buttons[0][0]['text'] = 'O'
            self.printBoard()
            self.playerMove()
            self.secondMove3()
        else:
            self.A[2][2] = 'O'
            self.ComputersMoveChange(2, 2)
            self.printBoard()
            self.playerMove()
            self.secondMove4()
    def secondMove1(self):
        if self.EnemyAttack() :
            pass
        elif self.A[0][0] == 'X':
            if self.A[1][2] == 'X' or self.A[2][1] == 'X': self.A[2][2] = 'O'
            else: self.A[2][1] = 'O'
            self.buttons[2][1]['text'] = 'O'
        elif self.A[0][2] == 'X':
            if self.A[1][0] == 'X' or self.A[2][1] == 'X': self.A[2][0] = 'O'
            else: self.A[2][1] = 'O'
            self.buttons[2][1]['text'] = 'O'
        elif self.A[2][0] == 'X':
            if self.A[1][2] == 'X' or self.A[0][1] == 'X': self.A[0][2] = 'O'
            else: self.A[0][1] = 'O'
            self.buttons[0][1]['text'] = 'O'
        elif self.A[2][2] == 'X':
            if self.A[0][1] == 'X' or self.A[1][0] == 'X': self.A[0][0] = 'O'
            else: self.A[0][1] = 'O'
            self.buttons[0][1]['text'] = 'O'
        self.printBoard()
        self.playerMove()
        self.thirdMove1()
    def secondMove2(self):
        if self.EnemyAttack() :
            pass
        elif self.A[2][2] == 'X':
            self.A[0][2] = 'O'
            self.buttons[0][2]['text'] = 'O'
        self.printBoard()
        self.playerMove()
        self.thirdMove2()
    def secondMove3(self):
        if self.EnemyAttack() :
            pass
        elif self.A[0][1] == 'X':
            if self.A[0][2] == 'X':
                self.A[1][0] = 'O'
                self.buttons[1][0]['text'] = 'O'
            elif self.A[1][2] == 'X':
                self.A[2][0] = 'O'
                self.buttons[2][0]['text'] = 'O'
            elif self.A[2][2] == 'X':
                self.A[2][1] = 'O'
                self.buttons[2][1]['text'] = 'O'
            elif self.A[1][0] == 'X':
                self.A[1][1] = 'O'
                self.buttons[1][1]['text'] = 'O'
            elif self.A[2][0] == 'X':
                self.A[2][1] = 'O'
                self.buttons[2][1]['text'] = 'O'
        elif self.A[1][0] == 'X':
            if self.A[2][0] == 'X':
                self.A[0][1] = 'O'
                self.buttons[0][1]['text'] = 'O'
            elif self.A[2][1] == 'X':
                self.A[0][2] = 'O'
                self.buttons[0][2]['text'] = 'O'
            elif self.A[2][2] == 'X':
                self.A[1][2] = 'O'
                self.buttons[1][2]['text'] = 'O'
            elif self.A[0][1] == 'X':
                self.A[1][1] = 'O'
                self.buttons[1][1]['text'] = 'O'
            elif self.A[0][2] == 'X':
                self.A[1][2] = 'O'
                self.buttons[1][2]['text'] = 'O'
        self.printBoard()
        self.playerMove()
        self.thirdMove3()
    def secondMove4(self):
        if self.EnemyAttack() :
            pass
        elif self.A[1][2] == 'X':
            if self.A[0][0] == 'X':
                self.A[1][0] = 'O'
                self.buttons[1][0]['text'] = 'O'
            elif self.A[0][1] == 'X':
                self.A[2][0] = 'O'
                self.buttons[2][0]['text'] = 'O'
            elif self.A[0][2] == 'X':
                self.A[2][1] = 'O'
                self.buttons[2][1]['text'] = 'O'
            elif self.A[2][0] == 'X':
                self.A[1][0] = 'O'
                self.buttons[1][0]['text'] = 'O'
            elif self.A[2][1] == 'X':
                self.A[1][1] = 'O'
                self.buttons[1][1]['text'] = 'O'
        elif self.A[2][1] == 'X':
            if self.A[0][0] == 'X':
                self.A[0][1] = 'O'
                self.buttons[0][1]['text'] = 'O'
            elif self.A[1][0] == 'X':
                self.A[0][2] = 'O'
                self.buttons[0][2]['text'] = 'O'
            elif self.A[2][0] == 'X':
                self.A[1][2] = 'O'
                self.buttons[1][2]['text'] = 'O'
            elif self.A[0][2] == 'X':
                self.A[0][1] = 'O'
                self.buttons[0][1]['text'] = 'O'
            elif self.A[1][2] == 'X':
                self.A[1][1] = 'O'
                self.buttons[1][1]['text'] = 'O'
        self.printBoard()
        self.playerMove()
        self.thirdMove3()
    def thirdMove1(self):
        if self.PlayerError() == False:
            if self.EnemyAttack() == False:
                if self.A[0][0] == 'X' and self.A[2][0] != 'X':
                    self.A[2][0] = 'O'
                    self.buttons[2][0]['text'] = 'O'
                elif self.A[0][2] == 'X' and self.A[2][2] != 'X':
                    self.A[2][2] = 'O'
                    self.buttons[2][2]['text'] = 'O'
                elif self.A[2][0] == 'X' and self.A[2][2] != 'X':
                    self.A[2][2] = 'O'
                    self.buttons[2][2]['text'] = 'O'
                elif self.A[2][2] == 'X' and self.A[2][0] != 'X':
                    self.A[2][0] = 'O'
                    self.buttons[2][0]['text'] = 'O'
                else:
                    flag = False
                    for i, s in enumerate(self.A):
                        for j, t in enumerate(s):
                            if t == '-':
                                self.A[i][j] = 'O'
                                self.buttons[i][j]['text'] = 'O'
                                flag = True
                                break
                        if flag: break
        self.printBoard()
        if self.Winning():
            print('You lost')
            return
        self.playerMove()
        self.fourthMove()
    def thirdMove2(self):
        if self.PlayerError() == False:
            self.EnemyAttack()
        self.printBoard()
        if self.Winning():
            print('You lost')
            return
        self.playerMove()
        self.fourthMove()
    def thirdMove3(self):
        if self.PlayerError() == False:
            if self.EnemyAttack() == False:
                flag = False
                for i, s in enumerate(self.A):
                    for j, t in enumerate(s):
                        if t == '-':
                            self.A[i][j] = 'O'
                            self.buttons[i][j]['text'] = 'O'
                            flag = True
                            break
                    if flag: break
        self.printBoard()
        if self.Winning():
            print('You lost')
            return
        self.playerMove()
        self.fourthMove()
    def fourthMove(self):
        if self.PlayerError() == False:
            if self.EnemyAttack() == False:
                flag = False
                for i, s in enumerate(self.A):
                    for j, t in enumerate(s):
                        if t == '-':
                            self.A[i][j] = 'O'
                            self.buttons[i][j]['text'] = 'O'
                            flag = True
                            break
                    if flag: break
        self.printBoard()
        if self.Winning():
            print('You lost')
            return
        self.playerMove()
    def playerMove(self):
        pass
    def printBoard(self):
        for i in self.A:
            for j in i:
                print(j, end='')
            print()

tut = ChoiceTree()
tut.printBoard()
tut.playerMove()
tut.firstMove()
system('pause')


