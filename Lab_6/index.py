# -*- coding: utf-8 -*-
import random
import numpy as np
def MakeScheduleForClass(clas, n):
    schedule = []
    i = n
    while i < len(data):
        j = 0
        while j < int(data[i][1]):
            schedule.append([clas, data[i][0], data[i][2], data[i][3]])
            j += 1
        i += 1
    for i in schedule:
        if i[2] == '0':
            for j in data:
                if j[0] == clas:
                    i[2] = j[1]
                    break
        if i[3] == '0':
            i[3] = i[0]
    return random.sample(schedule, len(schedule))
def CountCoincidence(schedule, n):
    errors = []
    suberrors = []
    i = 0
    while i < len(schedule[0]):
        for j in range(n):
            lst = [schedule[j][i], schedule[j][i + 1], schedule[j][i + 2], schedule[j][i + 3]]
            for s, k in enumerate(lst):
                if lst.count(k) > 1:
                    suberrors.append(j + i)
                    break
        i += 4
    arr = np.array(schedule)
    arr = arr.transpose()
    for q, j in enumerate(arr[2]):
        for w, k in enumerate(j):
            if list(j).count(k) > 1:
                errors.append([w, q])
                break
    return [errors, suberrors]
def Mutate(schedule, errors):
    if len(errors) == 1:
        for j in range(3):
            gy = random.randint(8,11)
            schedule[j][errors[0]], schedule[j][gy] = schedule[j][gy], schedule[j][errors[0]]
    for i in range(len(errors)):
        for j in range(3):
            gy = random.randint(4,7)
            schedule[j][errors[i]], schedule[j][i + gy] = schedule[j][i + gy], schedule[j][errors[i]]
    return
def Crossover(schedule, errors):
    for i in errors:
        schedule[i[0]][i[1]], schedule[i[0]][random.randint(0, 19)] = schedule[i[0]][random.randint(0, 19)], schedule[i[0]][i[1]]
    return
def PrettyOutput(schedule, n):
    f = open("schedule.txt", "w")
    i = 0
    if len(schedule) < 19:
        while i < len(schedule[0]):
            if i == 0: f.write("Monday:\n")
            elif i == 4: f.write("Tuesday:\n")
            elif i == 8: f.write("Wednesday:\n")
            elif i == 12: f.write("Thursday:\n")
            elif i == 16: f.write("Friday:\n")
            if i % 4 == 0: f.write("1 lesson:\n")
            elif i % 4 == 1: f.write("2 lesson:\n")
            elif i % 4 == 2: f.write("3 lesson:\n")
            elif i % 4 == 3: f.write("4 lesson:\n")
            for j in range(n):
                for k in schedule[j][i]:
                    if k == 'Reading' or k == 'PT' or k == 'English' or k == 'Arts':
                        f.write(k + '\t\t')
                    else: f.write(k + '\t')
                f.write('\n')
            i += 1
    f.close()
f = open('data.txt', 'r')
n = 3
data = []
for line in f:
    data.append(line.strip().split(', '))
f.close()
while 1:
    schedule = []
    i = 0
    while i < n:
        schedule.append(MakeScheduleForClass(data[i][0], n))
        i += 1
    while CountCoincidence(schedule, n)[0] != []:
        Crossover(schedule, CountCoincidence(schedule, n)[0])
    temp = schedule[:]
    while CountCoincidence(schedule, n)[1] != []:
        if i > 100:
            break
        Mutate(schedule, CountCoincidence(schedule, n)[1])
        #print(CountCoincidence(schedule, n)[1])
        i += 1
    if CountCoincidence(schedule, n)[1] == []: break
    else: continue
#for i in schedule: print(i)
PrettyOutput(schedule, n)