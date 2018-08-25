import random
from os import system
import math
def SafeInput(flag):
    while 1:
        try:
            num = int(input())
            if num > 3 and num < 41:
                break
            else:
                print("Ви помилилися. Спробуйте знову. Число повинне бути мiж 4 i 40.")
                continue
        except ValueError:
            print("Ви помилилися. Спробуйте знову. Введiть, будь ласка, число.")
    return num
class Iter():
    def __init__(self, Pole):
        self.Pole = Pole       
        self.T = 50
        self.alpha = 0.95        
    def FireIteration(self):
        Pos = self.Pole.MixTwoElements()	# Міняю два елементи
        ds = self.Pole.CalcCountAttack(Pos) - self.Pole.CalcSelf()      # Теперішня мінус колишня (позиція)
        if ds < 0:
            self.Pole.Change(Pos)
        else:
            p = math.exp(- ds / self.T)            
            if p > random.random():
                self.Pole.Change(Pos)
            self.T = self.alpha * self.T
        return self.Pole.CalcSelf()
class Checkboard():
    def __init__(self, N):
        self.N = N
        self.Pos = list()
        for n in range(self.N):
            self.Pos.append(n)          # Заповнюю список селф.Поз послідовністю натуральних чисед
    def MixTwoElements(self):
        Pos = list()
        for p in self.Pos:
            Pos.append(p)            # По суті копіюю Селф.Поз в тимчасовий масив
        i = 0
        j = 0
        while i == j:		# Міняю рендомні два елементи
            i = random.randint(0, self.N - 1)
            j = random.randint(0, self.N - 1)
        Pos[i], Pos[j] = Pos[j], Pos[i]
        return Pos        # Повертаю новий масив порядку елементів
    def CalcCountAttack(self, Pos):
        res = 0        # Рахую кількість нападів ферзя на ферзя
        for n in range(self.N):
            k = n - 1		# Половина по верху, половина по низу, в один бік йдуть "дві стріли" бою
            while k >= 0:
                if Pos[k] == (Pos[n] + (n - k)):
                    res = res + 1
                if Pos[k] == (Pos[n] - (n - k)):
                    res = res + 1
                k = k - 1
            k = n + 1
            while k < self.N:
                if Pos[k] == (Pos[n] + (k - n)):
                    res = res + 1
                if Pos[k] == (Pos[n] - (k - n)):
                    res = res + 1
                k = k + 1                
        return res
    def CalcSelf(self):
        return self.CalcCountAttack(self.Pos)
    def Change(self, Pos):
        self.Pos = Pos
print("Введiть число: ", end = '')
board = Checkboard(SafeInput('Введiть число: '))
Run = Iter(board)
for n in range(10000):
    cur = Run.FireIteration() 
    if cur == 0:
        for i in range(len(board.Pos)):
            print(' _',end = '')
        print()
        for item in board.Pos:
            for i in range(len(board.Pos)):
                if i == item: print('|Q', end = '')
                else: print('|_', end = '')
            print('|')
        break
system('pause')
